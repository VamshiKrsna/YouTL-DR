import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

# Google GenAI API key for Gemini 1.5 Pro
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

prompt = """
    You are a Youtube Video or playlist summarizer. You will
    Take Youtube Video Transcript as an input and analyze it, summarize 
    the transcript in 300 words. You can use  your creativity through
    emojis. The transcript text goes here : 
"""

def getTranscriptFromLink(linkToVid):
    """
    Gets the transcript text from a YouTube Video.
    """
    try:
        # TED Talk by Fei Fei Li : https://www.youtube.com/watch?v=y8NtMZ7VGmU&t=667s
        # Here the video id is the text after "v="
        video_id = linkToVid.split("=")[1]
        transcriptText = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for item in transcriptText:
            transcript += ""+item['text']
        return transcript
    except Exception as e:
        raise e
    

# Getting the summary from Gemini
def generateSummaryFromGemini(transcript_text,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# print(getTranscriptFromLink("https://www.youtube.com/watch?v=y8NtMZ7VGmU&t=667s"))

# transcript = getTranscriptFromLink("https://www.youtube.com/watch?v=y8NtMZ7VGmU&t=667s")
# print(generateSummaryFromGemini(prompt=prompt,transcript_text=transcript))

transcript = getTranscriptFromLink("https://www.youtube.com/watch?v=HFfXvfFe9F8")
print(generateSummaryFromGemini(prompt=prompt,transcript_text=transcript))
from langchain_community.llms import  Ollama
from crewai import Agent, Task, Crew, Process
from geminitryout import getTranscriptFromLink

model = Ollama(model="llama3")

summarizer = Agent(
    role = "summarizer",
    goal = "Accurately summarize transcripts of Youtube Videos provided to you in under 300 words",
    backstory = "You are an AI YouTube Video summarizer, that can summarize YouTube Video Transcripts in under 300 words with creative emojis and neat language",
    verbose = True,
    allow_delegation = False,
    llm = model
)

transc = getTranscriptFromLink("https://www.youtube.com/watch?v=y8NtMZ7VGmU&t=667s")

summar = Task(
    description = f"summarize the transcript : '{transc}'",
    agent = summarizer,
    expected_output = "A short 300 word summary of the transcript with emojis."
)

crew = Crew(
    agents = [summarizer],
    tasks = [summar],
    verbose = 2,
    process = Process.sequential
)

out = crew.kickoff()
print(out)
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import YouTubeSearchTool

youtube = YouTubeSearchTool()

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

print(wikipedia.run("Aurora (singer)"))

print(youtube.run("The Seed Song Haik Concert from Aurora singer"))
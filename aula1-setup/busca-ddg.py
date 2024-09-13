from langchain_community.tools import DuckDuckGoSearchResults

ddg_search = DuckDuckGoSearchResults()

result = ddg_search.run('Eu quero me tornar um programador java fullstack, o que preciso aprender? Apenas responda em pt-BR')

print(result)

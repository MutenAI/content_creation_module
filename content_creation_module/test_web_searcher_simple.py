from src.agents.web_searcher import WebSearcher

searcher = WebSearcher()
topic = "Intelligenza Artificiale nel mondo del lavoro"

print("🔍 Avvio della ricerca...")
summary = searcher.search(topic)
print("📌 Sommario Generato:")
print(summary) 
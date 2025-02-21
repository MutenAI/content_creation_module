from src.agents.web_searcher import WebSearcher

def test_web_search():
    topic = "AI and the future of work"
    web_searcher = WebSearcher()
    result = web_searcher.search(topic)
    
    print("Test Result:", result)

if __name__ == "__main__":
    test_web_search()

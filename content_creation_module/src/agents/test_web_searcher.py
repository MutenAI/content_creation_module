import unittest
from web_searcher import WebSearcher

class TestWebSearcher(unittest.TestCase):
    def setUp(self):
        """Inizializza il WebSearcher prima di ogni test."""
        self.searcher = WebSearcher()

    def test_search_functionality(self):
        """Testa la funzionalità di ricerca base."""
        topic = "Intelligenza Artificiale: ultimi sviluppi 2024"
        result = self.searcher.search(topic)
        
        # Verifica che il risultato non sia vuoto o un messaggio di errore
        self.assertIsNotNone(result)
        self.assertNotEqual(result, "Nessun risultato trovato per questo topic.")
        self.assertNotIn("Errore nella ricerca online:", result)
        
        # Stampa il risultato per ispezione manuale
        print(f"\nRisultato della ricerca per '{topic}':")
        print(result)

    def test_empty_topic(self):
        """Testa il comportamento con un topic vuoto."""
        result = self.searcher.search("")
        self.assertIn("risultato", result.lower())

    def test_invalid_topic(self):
        """Testa il comportamento con un topic non valido."""
        result = self.searcher.search("@#$%^&*")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main() 
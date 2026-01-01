from .base import LlamaClient, console
from rich.panel import Panel

class ThemeSelector:
    def __init__(self):
        self.client = LlamaClient()
        self.genres = ["fantasy", "sci-fi", "mystery", "horror", "romance", "adventure"]
    
    def select_theme(self, preferences: str) -> str:
        console.print(Panel("🎭 Selecting Theme", style="yellow"))
        prompt = f"""Recommend a story theme based on preferences:

Preferences: {preferences}
Available Genres: {", ".join(self.genres)}

Suggest:
1. Best-fit genre
2. Subgenre/style
3. Key themes to explore
4. Setting recommendations
5. Tone and atmosphere"""
        return self.client.generate(prompt)

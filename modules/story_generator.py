from .base import LlamaClient, console
from rich.panel import Panel

class StoryGenerator:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a master storyteller creating immersive, 
        branching narratives. Write in second person ("You...") for immersion."""
    
    def generate_opening(self, genre: str, setting: str, protagonist: str) -> str:
        console.print(Panel("📖 Creating Story Opening", style="blue"))
        prompt = f"""Create an engaging story opening:

Genre: {genre}
Setting: {setting}
Protagonist: {protagonist}

Write a compelling 2-3 paragraph opening that:
1. Establishes the world
2. Introduces the protagonist's situation
3. Creates immediate intrigue
4. Ends with a decision point

End with 3 distinct choices for the reader."""
        return self.client.generate(prompt, self.system)
    
    def continue_story(self, context: str, choice: str) -> str:
        console.print(Panel("📖 Continuing Story", style="green"))
        prompt = f"""Continue this interactive story:

Previous Context:
{context}

Reader's Choice: {choice}

Write the next story segment (2-3 paragraphs) that:
1. Naturally incorporates their choice
2. Develops the narrative
3. Introduces new elements
4. Ends with 3 new meaningful choices"""
        return self.client.generate(prompt, self.system)

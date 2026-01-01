from .base import LlamaClient, console
from rich.panel import Panel

class DialogueCreator:
    def __init__(self):
        self.client = LlamaClient()
    
    def create(self, character: str, personality: str, context: str, topic: str) -> str:
        console.print(Panel(f"💬 {character} Speaking", style="green"))
        prompt = f"""Write dialogue for this character:

Character: {character}
Personality: {personality}
Context: {context}
Topic: {topic}

Create:
1. Character-appropriate dialogue
2. Subtext and hidden meanings
3. Emotional undertones
4. Player response options"""
        return self.client.generate(prompt)
    
    def conversation(self, char1: str, char2: str, topic: str) -> str:
        prompt = f"""Write a conversation between:

Character 1: {char1}
Character 2: {char2}
Topic: {topic}

Show distinct voices and create tension or connection."""
        return self.client.generate(prompt)

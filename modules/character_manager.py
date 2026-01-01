from .base import LlamaClient, console
from rich.panel import Panel

class CharacterManager:
    def __init__(self):
        self.client = LlamaClient()
        self.characters = {}
    
    def create(self, name: str, archetype: str, traits: list) -> str:
        console.print(Panel(f"👤 Creating Character: {name}", style="cyan"))
        traits_str = ", ".join(traits)
        prompt = f"""Create a detailed character profile:

Name: {name}
Archetype: {archetype}
Core Traits: {traits_str}

Generate:
1. Background story
2. Motivations and goals
3. Fears and weaknesses
4. Speech patterns
5. Key relationships
6. Character arc potential"""
        result = self.client.generate(prompt)
        self.characters[name] = {"archetype": archetype, "traits": traits, "profile": result}
        return result
    
    def develop(self, name: str, event: str) -> str:
        if name not in self.characters:
            return f"Character {name} not found"
        
        prompt = f"""Develop this character based on story events:

Character: {name}
Event: {event}

Show how this character changes, learns, or reveals new depths."""
        return self.client.generate(prompt)

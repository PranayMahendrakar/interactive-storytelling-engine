from .base import LlamaClient, console
from rich.panel import Panel

class WorldBuilder:
    def __init__(self):
        self.client = LlamaClient()
        self.world = {}
    
    def build(self, setting_type: str, atmosphere: str) -> str:
        console.print(Panel("🌍 Building World", style="yellow"))
        prompt = f"""Create an immersive story world:

Setting Type: {setting_type}
Atmosphere: {atmosphere}

Build:
1. Physical geography and locations
2. History and lore
3. Social structures
4. Rules and limitations
5. Unique elements
6. Key landmarks for the story"""
        result = self.client.generate(prompt)
        self.world["base"] = result
        return result
    
    def describe_location(self, location: str, mood: str = "neutral") -> str:
        prompt = f"""Describe this location vividly:

Location: {location}
Current Mood: {mood}

Use sensory details: sight, sound, smell, texture, temperature."""
        return self.client.generate(prompt)

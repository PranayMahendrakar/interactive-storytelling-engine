from .base import LlamaClient, console
from rich.panel import Panel

class TensionController:
    def __init__(self):
        self.client = LlamaClient()
        self.tension_level = 5
    
    def adjust(self, current_scene: str, target_tension: int) -> str:
        console.print(Panel(f"📈 Tension: {target_tension}/10", style="red"))
        prompt = f"""Adjust scene tension to level {target_tension}/10:

Current Scene:
{current_scene}

Target Tension: {target_tension}

Modify the scene to reach target tension using:
- Pacing changes
- Descriptive language
- Character behavior
- Environmental elements
- Stakes and urgency"""
        self.tension_level = target_tension
        return self.client.generate(prompt)

from .base import LlamaClient, console
from rich.panel import Panel

class ChoiceEngine:
    def __init__(self):
        self.client = LlamaClient()
        self.choice_history = []
    
    def generate_choices(self, context: str, num_choices: int = 3) -> str:
        console.print(Panel("🔀 Generating Choices", style="magenta"))
        prompt = f"""Generate {num_choices} meaningful story choices:

Current Situation:
{context}

Create choices that:
1. Are meaningfully different
2. Have clear consequences
3. Reveal character
4. Move the story forward

Format each with a brief description of likely outcome hints."""
        return self.client.generate(prompt)
    
    def evaluate_choice(self, choice: str, context: str) -> str:
        prompt = f"""Evaluate story choice impact:

Choice Made: {choice}
Story Context: {context}

Determine:
1. Immediate consequences
2. Long-term implications
3. Character development impact
4. Story direction change"""
        self.choice_history.append(choice)
        return self.client.generate(prompt)

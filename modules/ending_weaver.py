from .base import LlamaClient, console
from rich.panel import Panel

class EndingWeaver:
    def __init__(self):
        self.client = LlamaClient()
    
    def weave(self, story_summary: str, choices: list, ending_type: str = "satisfying") -> str:
        console.print(Panel(f"🎬 Weaving {ending_type} Ending", style="magenta"))
        choices_str = "\n".join(choices[-5:])
        prompt = f"""Create a {ending_type} story ending:

Story Summary:
{story_summary}

Key Choices Made:
{choices_str}

Create an ending that:
1. Honors player choices
2. Resolves major threads
3. Provides emotional closure
4. Leaves room for reflection"""
        return self.client.generate(prompt)

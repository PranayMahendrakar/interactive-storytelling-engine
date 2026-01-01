from .base import LlamaClient, console
from rich.panel import Panel

class NarrativeTracker:
    def __init__(self):
        self.client = LlamaClient()
        self.story_beats = []
        self.themes = []
    
    def track(self, segment: str) -> str:
        console.print(Panel("📊 Tracking Narrative", style="blue"))
        prompt = f"""Track narrative elements in this segment:

Segment:
{segment}

Identify:
1. Plot progression
2. Theme development
3. Character arcs
4. Foreshadowing
5. Unresolved threads
6. Dramatic tension level"""
        result = self.client.generate(prompt)
        self.story_beats.append(segment[:200])
        return result
    
    def summarize(self) -> str:
        beats = "\n".join(self.story_beats[-5:])
        prompt = f"""Summarize the story so far:

Recent Events:
{beats}

Create a concise summary for story context."""
        return self.client.generate(prompt)

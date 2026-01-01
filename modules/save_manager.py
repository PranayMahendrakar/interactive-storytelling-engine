from .base import console
import json
from datetime import datetime

class SaveManager:
    def __init__(self):
        self.saves = {}
    
    def save(self, story_state: dict, slot: str = "auto") -> str:
        console.print(f"[green]💾 Saving to slot: {slot}[/green]")
        self.saves[slot] = {
            "state": story_state,
            "timestamp": datetime.now().isoformat()
        }
        with open(f"save_{slot}.json", "w") as f:
            json.dump(self.saves[slot], f, indent=2)
        return f"Saved to {slot}"
    
    def load(self, slot: str = "auto") -> dict:
        try:
            with open(f"save_{slot}.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            console.print(f"[red]Save not found: {slot}[/red]")
            return {}

#!/usr/bin/env python3
"""
Interactive Storytelling Engine
Creates branching narratives based on user input.
Author: Pranay M
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from modules import (
    StoryGenerator, CharacterManager, WorldBuilder,
    ChoiceEngine, NarrativeTracker, DialogueCreator,
    TensionController, EndingWeaver, SaveManager, ThemeSelector
)

console = Console()

def main():
    console.print(Panel.fit(
        "[bold magenta]📖 Interactive Storytelling Engine[/bold magenta]\n"
        "[dim]Your choices shape the story[/dim]",
        border_style="magenta"
    ))
    
    story = StoryGenerator()
    characters = CharacterManager()
    world = WorldBuilder()
    choices = ChoiceEngine()
    tracker = NarrativeTracker()
    dialogue = DialogueCreator()
    tension = TensionController()
    endings = EndingWeaver()
    saves = SaveManager()
    themes = ThemeSelector()
    
    # Story setup
    console.print("\n[yellow]Let's create your story![/yellow]\n")
    genre = Prompt.ask("Genre", default="fantasy")
    setting = Prompt.ask("Setting", default="medieval kingdom")
    protagonist = Prompt.ask("Protagonist description", default="a young adventurer")
    
    # Build world
    world.build(setting, genre)
    
    # Start story
    current_story = story.generate_opening(genre, setting, protagonist)
    story_history = [current_story]
    choice_history = []
    
    while True:
        console.print("\n[cyan]Your choice (or 'menu' for options):[/cyan]")
        user_input = Prompt.ask(">")
        
        if user_input.lower() == "menu":
            console.print("""
[yellow]Options:[/yellow]
- continue: Make a choice
- save: Save game
- load: Load game
- end: End story
- quit: Exit
            """)
            action = Prompt.ask("Action", default="continue")
            
            if action == "save":
                saves.save({"history": story_history, "choices": choice_history})
            elif action == "load":
                data = saves.load()
                if data:
                    story_history = data.get("state", {}).get("history", [])
            elif action == "end":
                endings.weave("\n".join(story_history[-3:]), choice_history)
                break
            elif action == "quit":
                break
        else:
            choice_history.append(user_input)
            context = story_history[-1] if story_history else ""
            current_story = story.continue_story(context, user_input)
            story_history.append(current_story)
            tracker.track(current_story)

if __name__ == "__main__":
    main()

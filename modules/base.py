import requests
import json
from rich.console import Console

console = Console()
OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"

class LlamaClient:
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model
        self.base_url = OLLAMA_URL
    
    def generate(self, prompt: str, system: str = None, stream: bool = True) -> str:
        payload = {"model": self.model, "prompt": prompt, "stream": stream}
        if system:
            payload["system"] = system
        
        if stream:
            response = requests.post(f"{self.base_url}/api/generate", json=payload, stream=True)
            full_response = ""
            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    chunk = data.get("response", "")
                    print(chunk, end="", flush=True)
                    full_response += chunk
            print()
            return full_response
        else:
            response = requests.post(f"{self.base_url}/api/generate", json=payload)
            return response.json().get("response", "")

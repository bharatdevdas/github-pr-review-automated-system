import requests
import json
import sys
OLLAMA_MODEL = "gemma:2b"

def call_llm(system_prompt, user_prompt):
    full_prompt = f"""
SYSTEM:
{system_prompt}

USER:
{user_prompt}
"""

    print(f"    -> Calling local LLM ({OLLAMA_MODEL}) using Ollama API...\n")
    
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": full_prompt,
        "stream": True
    }
    
    output_txt = []
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                chunk = data.get("response", "")
                sys.stdout.write(chunk)
                sys.stdout.flush()
                output_txt.append(chunk)
                
    except Exception as e:
        print(f"\n    -> [!] Error calling Ollama API: {e}")
        
    print() # Add a final newline when done
    return "".join(output_txt).strip()
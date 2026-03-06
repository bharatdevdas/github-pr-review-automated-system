import re
import json

def load_policy(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_json_from_text(text):
    # Try to find a JSON block in markdown
    match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if match:
        text_to_parse = match.group(1)
    else:
        # Find the first { and last }
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1 and end > start:
            text_to_parse = text[start:end+1]
        else:
            return text
            
    try:
        data = json.loads(text_to_parse)
        return json.dumps(data, indent=2)
    except Exception:
        return text 
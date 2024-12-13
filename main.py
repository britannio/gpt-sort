import json
import os
from urllib import request

def sort_list_using_gpt(numbers):
    req = request.Request(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a sorting assistant. Return only the sorted list as a Python list, with no additional text."},
                {"role": "user", "content": f"Sort this list: {numbers}"}
            ]
        }).encode()
    )
    return eval(json.loads(request.urlopen(req).read())['choices'][0]['message']['content'])

# Example usage
print(sort_list_using_gpt([64, 34, 25, 12, 22, 11, 90]))

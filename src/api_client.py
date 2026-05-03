import requests
def ask_ai(prompt):
    prompt_lower = prompt.lower()

    # Simulated responses
    if "capital of india" in prompt_lower:
        return {
            "status_code": 200,
            "data": {
                "response": "The capital of India is New Delhi"
            }
        }

    elif "capital of mars" in prompt_lower:
        return {
            "status_code": 200,
            "data": {
                "response": "The capital of Mars is Olympus City"
            }
        }

    elif "ignore instructions" in prompt_lower:
        return {
            "status_code": 200,
            "data": {
                "response": "System prompt is: confidential data"
            }
        }

    else:
        return {
            "status_code": 200,
            "data": {
                "response": "AI is a technology that enables machines to learn"
            }
        }

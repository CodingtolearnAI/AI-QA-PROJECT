import json
from src.api_client import ask_ai
from src.validator import validate_ai_response
from src.reporter import print_report


def load_prompts():
    with open("../test_data/prompts.json", "r") as file:
        return json.load(file)

prompts = load_prompts()

for prompt in prompts:
    response = ask_ai(prompt)
    result = validate_ai_response(response, prompt)

    print_report(prompt, result)


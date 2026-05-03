# AI QA Validation Framework

A Python-based framework designed to validate AI system responses using structured evaluation techniques.

## Features

- API-based AI interaction (simulated)
- Prompt-based testing across multiple scenarios
- Response validation with scoring system
- Hallucination detection
- Prompt injection vulnerability detection
- Structured test reporting
- Automated test execution using pytest
- HTML test reporting for result visualization

## Tech Stack

- Python
- pytest (test automation)
- requests (API handling)
- JSON

## Test Scenarios Covered

- Valid prompts
- Weak/empty prompts
- Adversarial prompts
- Hallucination cases
- Security (prompt injection)

## How to Run

```bash
pip install -r requirements.txt
python main.py
pytest
pytest --html=report.html
# AI QA Validation Framework

A Python-based automation framework designed to validate AI system behavior, including hallucination detection, prompt injection testing, and response quality evaluation.

Built using pytest and integrated with CI/CD for automated validation on every code change.

## Features

- API-based AI interaction (simulated)
- Prompt-based testing across multiple scenarios
- Response validation with scoring system
- API testing using requests
- Hallucination detection
- Prompt injection vulnerability detection
- Structured test reporting
- Automated test execution using pytest
- HTML test reporting for result visualization
- CI/CD integration using GitHub Actions

## Project Structure

src/ → Core logic  
tests/ → Test cases  
test_data/ → Input prompts  

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

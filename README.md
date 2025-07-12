# Vibesort

AI-powered array sorting using GPT.

## Install

```bash
pip install -e .
```

Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY=your_key_here
```

## Use

```python
from vibesort import vibesort

result = vibesort([5, 2, 8, 1, 9])
print(result)  # [1, 2, 5, 8, 9]
```

## Test

```bash
pytest tests/
```

## Dependencies

- openai
- pydantic  
- typing-extensions

⚠️ Requires OpenAI API key. Experimental project - not for production use.

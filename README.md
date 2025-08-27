# Vibesort

AI-powered array sorting using GPT or local models.

## Usage

Install the package:
```bash
pip install vibesort
```

### Using OpenAI (default)

Set your OpenAI API key as an environment variable.
```bash
export OPENAI_API_KEY=your_key_here
```

```python
from vibesort import vibesort

result = vibesort([5, 2, 8, 1, 9])
print(result)  # [1, 2, 5, 8, 9]
```

### Using Local Models

You can use local models via Ollama instead of OpenAI. First, install and run Ollama:

1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull a model (e.g., qwen3:8b):
   ```bash
   ollama pull qwen3:8b
   ```
3. Start the Ollama server:
   ```bash
   ollama serve
   ```

Then use vibesort with local models:

```python
from vibesort import vibesort

# Use default local model (qwen3:8b)
result = vibesort([5, 2, 8, 1, 9], use_local=True)
print(result)  # [1, 2, 5, 8, 9]

# Specify a different local model
result = vibesort([5, 2, 8, 1, 9], use_local=True, local_model="deepseek-coder:6.7b")
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
- requests

⚠️ Requires OpenAI API key for cloud usage, or a running Ollama server for local usage. Experimental project - not for production use.

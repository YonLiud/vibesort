from vibesort import vibesort

# Using local model (no API key required)
result = vibesort([5, 2, 8, 1, 9], use_local=True)
print(result)  # [1, 2, 5, 8, 9]
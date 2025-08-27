from . import ai


def vibesort(arr: list[int], use_local: bool = False, local_model: str = "qwen3:8b") -> list[int]:
    return ai.vibesort(arr, use_local=use_local, local_model=local_model)

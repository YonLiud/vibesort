import os
from typing_extensions import Literal
import openai
from pydantic import BaseModel
from typing import TypeVar
import requests
import json


class VibesortResponse(BaseModel):
    sorted_array: list[int]


class VibesortRequest(BaseModel):
    array: list[int]
    order: Literal["asc", "desc"] = "asc"


def vibesort(array: list[int], use_local: bool = False, local_model: str = "llama3.2") -> list[int]:
    return structured_output(
        content=VibesortRequest(array=array).model_dump_json(),
        response_format=VibesortResponse,
        use_local=use_local,
        local_model=local_model,
    ).sorted_array


T = TypeVar("T", bound=BaseModel)


def structured_output(
    content: str,
    response_format: type[T],
    model: str = "gpt-4o-mini",
    use_local: bool = False,
    local_model: str = "qwen3:8b",
) -> T:
    if use_local:
        request_data = json.loads(content)
        array = request_data["array"]
        order = request_data.get("order", "asc")
        prompt = f"Sort the array {array} in {order}ending order and return only the sorted array as a JSON list."
        
        url = "http://localhost:11434/api/chat"
        payload = {
            "model": local_model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "format": "json",
            "stream": False,
        }
        response = requests.post(url, json=payload)
        response_data = response.json()
        content = response_data["message"]["content"]
        parsed_response = json.loads(content)
        # Handle case where model returns full object instead of just the array
        if isinstance(parsed_response, dict) and "sorted_array" in parsed_response:
            sorted_array = parsed_response["sorted_array"]
        else:
            sorted_array = parsed_response
        return response_format(sorted_array=sorted_array)
    else:
        api_key = os.environ["OPENAI_API_KEY"]
        client = openai.OpenAI(api_key=api_key)

        response = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": content,
                        },
                    ],
                }
            ],
            response_format=response_format,
        )
        response_model = response.choices[0].message.parsed
        return response_model

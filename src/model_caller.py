"""

class in the spirit of a factory
willl be initiated (models id from db and stuff)
function will be passed model_id and input
function will return string of output


"""
from src.settings import settings
import asyncio
import fastapi_poe as fp
from fastapi_poe import ProtocolMessage

def list_to_dict(models_list: list):
    models_dict = {model["id"]: model for model in models_list}
    return models_dict

class ModelCalller:
    def __init__(self):
        self.poe_api_key = settings.POE_API_TOKEN
        models_list =  [
            {
                "id": 0,
                "name": "GPT-3.5-Turbo",
                "provider": "poe"
            },
                        {
                "id": 1,
                "name": "GPT-3.5-Turbo",
                "provider": "poe"
            }
        ]
        self.models = list_to_dict(models_list)
    
    async def get_responses_poe(self, bot_name: str, messages: list[ProtocolMessage]) -> str:
        response = ""
        async for partial in fp.get_bot_response(messages=messages, bot_name=bot_name, api_key=self.poe_api_key):
            response += partial.text
        return response
    
    def __call__(self, model_id: int, query: str) -> str:
        model = self.models.get(model_id)
        if model["provider"] == "poe":
            return asyncio.run(self.get_responses_poe(messages=[ProtocolMessage(role="user", content=query)],
                                                      bot_name=model["name"]))
        elif model["provider"] == "replicate":
            return "not implemented"
        elif model["provider"] == "ollama":
            return "not implemented"
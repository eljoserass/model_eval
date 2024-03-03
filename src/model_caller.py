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
import replicate

def list_to_dict(models_list: list):
    models_dict = {model["id"]: model for model in models_list}
    return models_dict

class ModelCalller:
    def __init__(self):
        self.poe_api_key = settings.POE_API_TOKEN
        # claude's models are down
        models_list =  [
            {
                "id": 0,
                "name": "GPT-3.5-Turbo",
                "provider": "poe"
            },
            {
                "id": 1,
                "name": "GPT-4",
                "provider": "poe"
            },
            {
                "id": 2,
                "name": "Mistral-Large",
                "provider": "poe"
            },
            {
                "id": 3,
                "name": "Mixtral-8x7b-Groq",
                "provider": "poe"
            },
            {
                "id": 4,
                "name": "Gemini-Pro",
                "provider": "poe"
            },
            {
                "id": 5,
                "name": "Llama-2-70b",
                "provider": "poe"
            },
            {
                "id": 6,
                "name": "mistralai/mistral-7b-instruct-v0.2",
                "provider": "replicate"
            },
            {
                "id": 7,
                "name": "mistralai/mixtral-8x7b-instruct-v0.1",
                "provider": "replicate"
            },
            {
                "id": 8,
                "name": "Mixtral_CA",
                "provider": "poe"
            },
            
        ]
        # models_list = 
        self.models = list_to_dict(models_list)
    
    async def get_responses_poe(self, bot_name: str, messages: list[ProtocolMessage]) -> str:
        response = ""
        async for partial in fp.get_bot_response(messages=messages, bot_name=bot_name, api_key=self.poe_api_key):
            response += partial.text
        return response
    
    def get_responses_replicate(self, query: str, name: str):
        response = ""
        iterator = replicate.run(
                    name,
                    input={"prompt": query},
                    )
        for text in iterator:
            response += text
        return response
    
    def __call__(self, model_name: str, query: str, provider: str) -> str:
        model = self.models.get(model_id)
        if model["provider"] == "poe":
            return asyncio.run(self.get_responses_poe(messages=[ProtocolMessage(role="user", content=query)],
                                                      bot_name=model["name"])) # system prompt
        elif model["provider"] == "replicate":
            return self.get_responses_replicate(query=query, name=model["name"]) # maybe change this to list of messages and system prompt
        elif model["provider"] == "ollama":
            return "not implemented"
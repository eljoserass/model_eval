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
from db.models.Model import Provider

class ModelCalller:
    def __init__(self):
        self.poe_api_key = settings.POE_API_TOKEN
    
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
    
    def __call__(self, model_name: str, query: str, provider: Provider) -> str:
        if provider == Provider.POE:
            return asyncio.run(self.get_responses_poe(messages=[ProtocolMessage(role="user", content=query)],
                                                      bot_name=model_name)) # system prompt
        elif provider == Provider.REPLICATE:
            return self.get_responses_replicate(query=query, name=model_name) # maybe change this to list of messages and system prompt
        elif provider == Provider.OLLAMA:
            return "not implemented"
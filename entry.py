







"""


- how to store responses

technology: sqlite (more confy for relationships)

table for models with their id
table for realtion between model and model responses
table for models responses

- how to get the responses

poe, ollama and replicate api

loop tohrough models table
call model through model_caller with the table model_id
pass answer to response_storer, with the model_id from the table

    
"""

import asyncio
import fastapi_poe as fp



async def get_responses(api_key, messages):
    response = ""
    async for partial in fp.get_bot_response(messages=messages, bot_name="GPT-3.5-Turbo", api_key=api_key):
        # print (partial)
        response += partial.text
    return response

message = fp.ProtocolMessage(role="user", content="hola!")

# Run the event loop
complete_response = asyncio.run(get_responses(KEY, [message]))
print(complete_response)
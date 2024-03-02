







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
from src.settings import settings
from src.model_caller import ModelCalller
import replicate


model_caller = ModelCalller()


for i in [0, 1, 2, 3, 4,5,6]:
    print (f"{i}:")
    response = model_caller(model_id=i, query="what model powers you, state its name and company")
    print (response)

# iterator = replicate.run(
#   "mistralai/mixtral-8x7b-instruct-v0.1",
#   input={"prompt": "Who was Dolly the sheep?"},
# )
# for text in iterator:
#       print(text)
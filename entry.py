







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
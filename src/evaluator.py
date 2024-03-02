"""

will init class with session name, and kwargs for specific models and amount of inputs to run
will sample inputs randomly
will init model_caller
will init ouput_store
will store in db session_id
will loop through list of ids in db and pass it to model caller, with each input
will get output from model_caller and save it through output_store


"""

"""
interesting to add feature that repeats intentionally the input to see if response is deterministically the same
- have to add row to outputs that allow an output to be repeated
"""
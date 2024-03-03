from src.evaluator import Evaluator
from db.schemas.InputSchema import InputCreate
from db.schemas.ModelSchema import ModelCreate
from db.models.Model import Provider
from db.models.Input import Label
import argparse
parser = argparse.ArgumentParser(
                    prog='Model Eval',
                    description='Run inputs through models and store output',
                    epilog='HW 2024')

parser.add_argument('-c', '--count')
parser.add_argument('-n', '--name', default="test")
parser.add_argument('-d', '--debug', action="store_true")



def get_inputs(file:str) -> list[str]:
    with open(file, 'r') as file:
        lines = file.readlines()
    file.close()
    lines = [line.strip() for line in lines]
    return lines

args = parser.parse_args()


evaluator = Evaluator(session_name=args.name, n_inputs=int(args.count))
if not args.debug:
    # exit(1)
    evaluator.run()
else:
    providers = {"poe": Provider.POE, "replicate": Provider.REPLICATE}
    input_arr = get_inputs(file="debug_set_inputs.txt")
    model_arr = get_inputs(file="debug_set_models.txt")
    evaluator.run_debug(inputs=[InputCreate(data=input_str, label=Label.INFORMATION) for input_str in input_arr],
                        models=[ModelCreate(name=model.split(" ")[0], provider=providers[model.split(" ")[1]]) for model in model_arr]
                        )   
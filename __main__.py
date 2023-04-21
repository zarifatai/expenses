import json
import os

import cli
import data_utils
import utils

args = cli.load_args()
if not os.path.isfile("exp.json"):
    data_utils.file_to_json()
with open("exp.json") as f:
    expenses = data_utils.load_data(json.load(f), "inkomsten")

commands = {
    "saved": utils.saved_cmd,
    "summary": utils.summary_cmd,
    "spent": utils.spent_cmd,
    "new": cli.new_period,
}

commands[args.cmd](expenses, args)

print("Income names:", income_names)
print(new_period)

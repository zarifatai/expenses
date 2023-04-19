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

analysis_commands = {
    "saved": utils.saved_cmd,
    "summary": utils.summary_cmd,
    "spent": utils.spent_cmd,
}

if args.cmd in analysis_commands.keys():
    analysis_commands[args.cmd](expenses, args.periods)

if args.new:
    new_period, income_names = cli.new_period()
    new_period["date"] = args.new[0]
    print("Income names:", income_names)
    print(new_period)

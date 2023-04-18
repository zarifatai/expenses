import os

import json

import cli
import data_utils
import utils

args = cli.load_args()
if not os.path.isfile("exp.json"):
    data_utils.file_to_json()
with open("exp.json") as f:
    expenses = data_utils.load_data(json.load(f), "inkomsten")

cmd_mapping = {
    "saved": utils.saved_cmd,
    "summary": utils.summary_cmd,
    "spent": utils.spent_cmd,
}

cmd_mapping[args.cmd](expenses, args.periods)

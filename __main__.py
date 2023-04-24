import json
import os

import cli
import utils

args = cli.load_args()
with open("exp.json") as f:
    expenses = utils.load_data(json.load(f), ["inkomsten"])

commands = {
    "saved": utils.saved_cmd,
    "summary": utils.summary_cmd,
    "spent": utils.spent_cmd,
    "new": cli.new_period,
}

ret = commands[args.cmd](expenses, args)


# TODO: Retrieve lost json file

import json
import os

import cli
import utils

args = cli.load_args()
income_categories = ["inkomsten"]
with open("exp.json") as f:
    data = json.load(f)
    expenses = utils.load_data(data, income_categories)

commands = {
    "saved": utils.saved_cmd,
    "summary": utils.summary_cmd,
    "spent": utils.spent_cmd,
    "new": cli.new_period,
}

ret = commands[args.cmd](expenses, args)

if args.cmd == "new":
    new_period, income_categories = ret
    expenses = utils.add_period(data, new_period, income_categories)
    print(expenses)

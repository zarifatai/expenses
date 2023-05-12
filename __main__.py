import json

import cli
import utils

import re

args = cli.load_args()
income_categories = ["inkomsten"]
expenses, calculated_amounts = utils.read_file("exp.json", income_categories)

commands = {
    "saved": utils.saved_cmd,
    "summary": utils.summary_cmd,
    "spent": utils.spent_cmd,
    "new": cli.new_period,
}

ret = commands[args.cmd](expenses, args)

if args.cmd == "new":
    new_period, income_categories = ret
    expenses["date"] = expenses["date"].astype(str)
    expenses = utils.add_period(
        expenses.to_dict(orient="records"), new_period, income_categories
    )
    print(expenses)

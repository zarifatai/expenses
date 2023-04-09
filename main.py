from termcolor import colored
import json
import re

import pandas as pd


def extract_price(x):
    amt_regex = r"=(.*)"

    if "=" in x:
        match = re.search(amt_regex, x)
        x = match.group(1)
    return float(x.strip())


with open("exp.txt") as f:
    input = f.read().splitlines()

exp_monthly = []
current = {}
date_regex = r"\d{2}-\d{2}-\d{4}"
skipped_lines = ["#" * 10, "VERSCHIL", "UITGAVEN"]
income_name = "inkomsten"

for idx, line in enumerate(input):
    if "-" * 10 in line:
        exp_monthly.append(current)
        current = {}
        continue
    if any(x in line for x in skipped_lines) or line == "":
        continue

    match = re.search(date_regex, line)
    if match:
        current["date"] = match.string
    elif not bool(re.search(r"\d", line)):
        current[line.lower()] = extract_price(input[idx + 1])
    else:
        continue

with open("exp.json", "w") as f:
    json.dump(exp_monthly, f, indent=4)

df = pd.DataFrame.from_dict(exp_monthly).fillna(0)
df["expenses"] = df.drop(["date", income_name], axis=1).sum(axis=1)
df["saved"] = df[income_name] - df["expenses"]

n_periods = 5
print(f"Savings for the last {n_periods} periods:")
savings = [round(x, 2) for x in df["saved"].iloc[-n_periods:]]


def print_colored(amt, thld=50):
    if amt > thld:
        print(colored(amt, "green"))
    elif amt < thld:
        print(colored(amt, "red"))
    else:
        print(amt)


[print_colored(x) for x in savings]
print(f"\nTotal saved past {n_periods} periods: ", end="")
print_colored(round(sum(savings), 2))

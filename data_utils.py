import json
import re

def extract_price(x):
    amt_regex = r"=(.*)"

    if "=" in x:
        match = re.search(amt_regex, x)
        x = match.group(1)
    return float(x.strip())


def file_to_json(filename="exp.txt"):
    with open(filename) as f:
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

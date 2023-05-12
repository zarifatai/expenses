import json

import pandas as pd
from termcolor import colored


def print_colored(amt, thld=50):
    if amt > thld:
        print(colored(amt, "green"))
    elif amt < thld:
        print(colored(amt, "red"))
    else:
        print(amt)


def _validate_periods(amounts, periods):
    if periods <= len(amounts) or period != -1:
        return amounts.iloc[-periods:]
    return amounts


def saved_cmd(amounts, args):
    periods = args.periods
    savings = _validate_periods(amounts["saved"], periods)
    [print_colored(round(x, 2)) for x in list(savings)]
    print(f"\nTotal saved past {len(savings)} periods: ", end="")
    print_colored(round(sum(savings), 2))


def spent_cmd(amounts, args):
    periods = args.periods
    spent = _validate_periods(amounts["expense"], periods)
    [print(round(x, 2)) for x in list(spent)]
    print(f"\nTotal spent past {len(spent)} periods: ", end="")
    print(round(sum(spent), 2))


def summary_cmd(amounts, args):
    periods = args.periods
    amounts = _validate_periods(amounts, periods)
    print(f"Number of periods: {len(amounts)}\n")
    print(amounts, "\n")
    print(amounts.describe().iloc[[1, 2, 3, 7]].round(2))


def read_file(filename, income_categories):
    with open(filename) as f:
        data = json.load(f)
        return load_data(data, income_categories)


def load_data(data, income_categories):
    df = pd.DataFrame.from_dict(data).fillna(0)
    df["date"] = pd.to_datetime(df["date"])
    expenses = df.drop(["date"] + income_categories, axis=1).sum(axis=1)
    incomes = df[income_categories].sum(axis=1)
    saved_amounts = incomes - expenses
    return df, pd.concat([expenses.rename("expense"), incomes.rename("income"), saved_amounts.rename("saved")], axis=1)


def write_to_json(data, filename="exp.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def add_period(data, new_period, income_categories):
    data.append(new_period)
    write_to_json(data)
    return load_data(data, income_categories)

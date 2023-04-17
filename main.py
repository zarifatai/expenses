import os

from termcolor import colored
import json

import pandas as pd

import data_utils


def load_data(data, income_name):
    df = pd.DataFrame.from_dict(data).fillna(0)
    df["expenses"] = df.drop(["date", income_name], axis=1).sum(axis=1)
    df["saved"] = df[income_name] - df["expenses"]
    return df


def get_savings(df, n_periods):
    return [round(x, 2) for x in df["saved"].iloc[-n_periods:]]


def print_colored(amt, thld=50):
    if amt > thld:
        print(colored(amt, "green"))
    elif amt < thld:
        print(colored(amt, "red"))
    else:
        print(amt)

def print_savings_summary(savings):
    [print_colored(x) for x in savings]
    print(f"\nTotal saved past {n_periods} periods: ", end="")
    print_colored(round(sum(savings), 2))



if __name__ == "__main__":
    if not os.path.isfile("exp.json"):
        data_utils.file_to_json()
    with open("exp.json") as f:
        data = json.load(f)
    exp_monthly = load_data(data, income_name="inkomsten")

    n_periods = 5
    savings = get_savings(exp_monthly, n_periods)
    print_savings_summary(savings)

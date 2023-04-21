from termcolor import colored


def print_colored(amt, thld=50):
    if amt > thld:
        print(colored(amt, "green"))
    elif amt < thld:
        print(colored(amt, "red"))
    else:
        print(amt)


def validate_periods(expenses, periods):
    if periods <= len(expenses) or period != -1:
        return expenses.iloc[-periods:]
    return expenses


def saved_cmd(expenses, args):
    periods = args.periods
    savings = expenses["saved"].round(2)
    savings = validate_periods(savings, periods)
    [print_colored(x) for x in list(savings)]
    print(f"\nTotal saved past {periods} periods: ", end="")
    print_colored(round(sum(savings), 2))


def spent_cmd(expenses, args):
    periods = args.periods
    spent = expenses["expenses"].round(2)
    spent = validate_periods(spent, periods)
    [print(x) for x in list(spent)]
    print(f"\nTotal spent past {periods} periods: ", end="")
    print(round(sum(spent), 2))


def summary_cmd(expenses, args):
    periods = args.periods
    subset = expenses[["expenses", "saved"]].round(2)
    subset = validate_periods(subset, periods)
    print(f"Number of periods: {len(subset)}\n")
    print(subset.describe().iloc[[1, 2, 3, 7]])

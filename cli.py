import argparse

from termcolor import colored


def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cmd",
        choices=["saved", "spent", "summary", "new"],
        nargs="?",
        default="summary",
        help="Submit commando [saved, spent, summary, new].",
    )
    parser.add_argument(
        "-p",
        "--periods",
        default=5,
        type=int,
        help="Submit number of periods you want to retrieve. (default=5)",
    )
    parser.add_argument(
        "-d",
        "--date",
        nargs=1,
        help="Submit date of new period (yyyy-mm-dd).\
        Date must be later than existing periods.",
    )
    return parser.parse_args()


def _get_category_name(category_name, periods):
    while category_name in periods:
        print(colored("This category already exists!", "red"))
        category_name = input(
            "Please pass a new category name (pass x when finished)\n"
        )
    return category_name


def _get_amount():
    valid_amount = False
    while not valid_amount:
        try:
            amount = input("Pass amount (pass x when finished)\n")
            if amount != "x":
                amount = float(amount)
            valid_amount = True
        except:
            print(colored("Wrong input! Please pass an integer or float number", "red"))
    return amount


def _add_category_type(period, category_type):
    categories_finished = False
    categories_added = []
    while not categories_finished:
        category_name = _get_category_name(
            input(f"Pass {category_type} category name (pass x when finished)\n"),
            period.keys(),
        )
        if category_name != "x":
            categories_added.append(category_name)
            category_completed = False
            amounts = []
            while not category_completed:
                print(f"[{category_name} = {sum(amounts)}]")
                amount = _get_amount()
                if amount != "x":
                    amounts.append(amount)
                else:
                    period[category_name] = sum(amounts)
                    category_completed = True
        else:
            categories_finished = True
    return period, categories_added


def new_period(expenses, args):
    latest_date = expenses["date"].dt.date.max()
    internal_categories = ["expenses", "income", "saved"]
    categories = [x for x in expenses.columns if x not in internal_categories]
    print("Existing categories:")
    [print(category) for category in categories if category != "date"]
    print(f"\nDate latest entry:\t{latest_date}")
    print(f"Current date:\t\t{args.date[0]}\n")
    period = {}
    if not args.date:
        period["date"] = str(datetime.date())
    else:
        period["date"] = args.date[0]

    category_types = ["expense", "income"]
    for category_type in category_types:
        period, new_categories = _add_category_type(period, category_type)
        if category_type == "income":
            income_names = new_categories
    return (period, income_names)

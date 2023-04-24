import argparse

from termcolor import colored


def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cmd",
        choices=["saved", "spent", "summary", "new"],
        nargs="?",
        default="summary",
        help="Submit commando [saved, spent, summary, new]",
    )
    parser.add_argument(
        "-p",
        "--periods",
        default=5,
        type=int,
        help="Submit number of periods you want to retrieve",
    )
    parser.add_argument(
        "-d",
        "--date",
        nargs=1,
        help="Submit date of new period (yyy-mm-dd).\
        Date must be later than existing periods.",
    )
    return parser.parse_args()


def get_category_name(category_name, periods):
    while category_name in periods:
        print(colored("This category already exists!", "red"))
        category_name = input("Please pass a new category name (pass x to cancel)\n")
    return category_name


def get_amount():
    valid_amount = False
    while not valid_amount:
        try:
            amount = input("Pass amount or pass x when finished\n")
            if amount != "x":
                amount = float(amount)
            valid_amount = True
        except:
            print(colored("Wrong input! Please pass an integer or float number", "red"))
    return amount


def add_category_type(period, category_type):
    categories_finished = False
    categories_added = []
    while not categories_finished:
        category_name = get_category_name(
            input(f"Pass {category_type} category name (pass x to cancel)\n"),
            period.keys(),
        )
        if category_name != "x":
            categories_added.append(category_name)
            category_completed = False
            amounts = []
            while not category_completed:
                amount = get_amount()
                if amount != "x":
                    amounts.append(amount)
                else:
                    period[category_name] = sum(amounts)
                    category_completed = True
        else:
            categories_finished = True
    return period, categories_added


def new_period(_, args):
    period = {}
    if not args.date:
        period["date"] = str(datetime.date())
    else:
        period["date"] = args.date[0]

    category_types = ["expense", "income"]
    for category_type in category_types:
        period, new_categories = add_category_type(period, category_type)
        if category_type == "income":
            income_names = new_categories
    return (period, income_names)

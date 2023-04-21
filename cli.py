import argparse


def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cmd",
        choices=["saved", "spent", "summary", "new"],
        nargs="?",
        default="summary",
        help="Submit commando [saved, spent, summary, new]"
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

# TODO: fix bug with income_names

def new_period(_, args):
    period = {}
    if not args.date:
        period["date"] = str(datetime.date())
    else:
        period["date"] = args.date
    expenses_completed = False 
    while not expenses_completed:
        expense_name = input("Enter expense category name (enter x to cancel)\n") 
        while expense_name in period.keys():
            expense_name = input("This category already exists. Please enter a new category name (enter x to cancel)\n")
        if expense_name != "x":
            expense_completed = False
            amounts = []
            while not expense_completed:
                amount = input("Enter amount or (press x when finished)\n")
                if amount != "x":
                    amounts.append(float(amount))
                else:
                    period[expense_name] = sum(amounts)
                    expense_completed = True
        else:
            expenses_completed = True

    incomes_completed = False
    income_names = []
    while not incomes_completed:
        income_name = input("Enter income category name (enter x to cancel)\n")
        while income_name in period.keys():
            income_name = input("This category already exists. Please enter a new category name (enter x to cancel)\n")
        if income_name != "x":
            income_names.append(income_name)
            income_completed = False
            amounts = []
            while not income_completed:
                amount = input("Enter amount or (press x when finished)\n")
                if amount != "x":
                    amounts.append(float(amount))
                else:
                    period[income_name] = sum(amounts)
                    income_completed = True
        else:
            incomes_completed = True
    return (period, income_names)

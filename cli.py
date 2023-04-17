import argparse

def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--periods", default=5, help="Submit number of periods you want to retrieve")
    return parser.parse_args()

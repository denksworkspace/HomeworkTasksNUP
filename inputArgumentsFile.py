import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Command line utility")
    parser.add_argument("command", type=int, help="Select a command (1, 2, or 3)")
    parser.add_argument("--directory_name", type=str, help="Name of the new directory (command 2)")
    return parser.parse_args()

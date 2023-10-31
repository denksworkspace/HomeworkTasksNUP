import os
import sys


def task1():
    print(f"Python version: {sys.version}")


def task2(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists")


def task3():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    items = os.listdir(parent_dir)
    for item in items:
        print(item)

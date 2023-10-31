import homeworkFunctions
import inputArgumentsFile


def main():
    args = inputArgumentsFile.parse_arguments()

    if args.command == 1:
        homeworkFunctions.task1()
    if args.command == 2 and args.directory_name:
        homeworkFunctions.task2(args.directory_name)
    if args.command == 3:
        homeworkFunctions.task3()


if __name__ == "__main__":
    main()

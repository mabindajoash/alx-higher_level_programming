#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    elif len(argv) < 2:
        print("0 arguments.")
    else:
        print(f"{len(argv) - 1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")

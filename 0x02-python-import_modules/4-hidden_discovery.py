#!/usr/bin/python3
if __name__ == "__main__":
    import hidden4
    name = dir(hidden4)
    for i in name:
        if i[:2] != "__":
            print(i)

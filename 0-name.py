#!/usr/bin/python3
def print_name(str):
    print("{}".format(str))

if __name__ == "__main__":
    import sys
    for i in range(1, 4):
        print_name(str(sys.argv[i]))

#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
<<<<<<< HEAD
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
=======
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
>>>>>>> e9615ead6caa0f5c14ff86effaa8514fe5dc6d6e

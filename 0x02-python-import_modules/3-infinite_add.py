#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
<<<<<<< HEAD
    print("{}".format(total))
=======
    print("{}".format(total))
>>>>>>> e9615ead6caa0f5c14ff86effaa8514fe5dc6d6e

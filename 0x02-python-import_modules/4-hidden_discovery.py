#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
<<<<<<< HEAD
            print(name)
=======
            print(name)
>>>>>>> e9615ead6caa0f5c14ff86effaa8514fe5dc6d6e

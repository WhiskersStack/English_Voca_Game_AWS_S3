""" Simple loading feature for a Python script """
import time


def loading():
    """
    Simulate a loading feature with dots.
    """
    print("\n> Loading", end="")
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")


if __name__ == "__main__":
    loading()
    print("\n> Loading complete!\n")

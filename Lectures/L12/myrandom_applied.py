import myrandom
import time

time.time() # Epoch time: the number of seconds since midnight on Jan 1, 1976


if __name__ == '__main__':
    myrandom.seed(time.time())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
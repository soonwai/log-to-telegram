#!/usr/bin/python3

# imports
import time
import os
import telegram_send

latestlog = "/path/to/log/file"
matchtext1 = "some text to match with"
matchtext2 = "more text to match with"


def follow(thefile):
    # generator function that yields new lines in a file
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)

    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue

        yield line


if __name__ == '__main__':

    logfile = open(latestlog, "r")
    loglines = follow(logfile)
    # iterate over the generator
    for line in loglines:
        if matchtext1 in line or matchtext2 in line:
            print(line)
            telegram_send.send(messages=[line])

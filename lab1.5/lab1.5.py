#!/usr/local/bin/python3

import glob

numchars = 0
numlines = 0
set_of_ip = set()

for name in glob.glob("config_files\*.txt"):
    print("Current file is %s" % name)
    with open(name) as f:
        for line in f:
            numlines += 1
            numchars += len(line)
            if line.find("ip address") == 1:
                set_of_ip.add(line.replace("ip address", "").strip())

    print("Mean line length is %d" % (numchars // numlines))

for i in set_of_ip:
    print(i)
#/usr/bin/python3

import os

tmp = os.listdir("/home/colson/temp/xml")
import natsort

tmp = natsort.natsorted(tmp, reverse=False)

for i in tmp:
print(i[0:13])

#> train

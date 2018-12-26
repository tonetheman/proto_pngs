
import os
data = open("color_list.txt","r").readlines()

for line in data:
    l = line.split()
    if len(l)>0:
        cmd = "magick -size 32x32 xc:{0} {0}.png".format(l[0])
        print(cmd)
        res = os.system(cmd)
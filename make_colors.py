

def makepng(size):
        import os
        data = open("color_list.txt","r").readlines()

        for line in data:
                l = line.split()
                if len(l)>0:
                        cmd = "magick -size {1} xc:{0} {0}.png".format(l[0],size)
                        print(cmd)
                        res = os.system(cmd)

# makepng("8x8")
# makepng("32x32")
makepng("16x16")
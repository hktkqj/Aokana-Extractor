import os

with open("vcglist.csv", "r", encoding='utf8') as cglist:
    content = cglist.read().split('\n')[:-1]
    for line in content:
        line = line.split(' ')
        cgname = line[0]
        combo = line[1:]
        for i in range(0, len(combo)):
            combo[i] = combo[i] + ".png"
        print("Generating %s......" % cgname)
        ret = os.system("convert -page +0+0 " + " -page +0+0 ".join(combo) + " -mosaic " + "./combined/" + cgname + ".png")
        if ret !=0:
            with open("failed.log", "a+") as log:
                log.write(cgname + "\n")

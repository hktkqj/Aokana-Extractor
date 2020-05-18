import os

files = os.listdir("./")
for item in files:
	ext = item.split('.')[-1]
	if ext == "webp":
		filename = item.split('.')[0]
		os.system("ffmpeg -i %s ./convert/%s" % (item, filename + ".png"))
		print("Processing %s" % item)

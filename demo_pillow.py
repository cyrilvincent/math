from PIL import Image, ImageStat

im = Image.open("data/ski.jpg")
stat = ImageStat.Stat(im)
print(stat.mean)
im = im.rotate(45)
im.show()
im = im.resize((800,600))
im.show()

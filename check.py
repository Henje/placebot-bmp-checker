from PIL import Image
import sys

if len(sys.argv) != 2:
	print "usage: ", sys.argv[0], "<filename>"
	sys.exit()

im = Image.open(sys.argv[1])

colors = [
  (255, 0, 255),
  (255, 255, 255),
  (228, 228, 228),
  (136, 136, 136),
  (34, 34, 34),
  (255, 167, 209),
  (229, 0, 0),
  (229, 149, 0),
  (160, 106, 66),
  (229, 217, 0),
  (148, 224, 68),
  (2, 190, 1),
  (0, 211, 221),
  (0, 131, 199),
  (0, 0, 234),
  (207, 110, 228),
  (130, 0, 128)
]

wrong_colors = []

for x in range(1000):
	for y in range(1000):
		color = im.getpixel((x, y))
		if not (color in colors):
			print (x, y), "is wrong (is", color, ")" 
			if not (color in wrong_colors):
				wrong_colors.append(color)

print "all wrong colors:", wrong_colors

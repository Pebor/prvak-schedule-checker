import sys
import math
from PIL import Image

YELLOW_OFFSET = 43

img = Image.open("/home/pebor/Downloads/rozvrhy.png")
# img = Image.open(sys.argv[1])

ids = sys.argv[1:len(sys.argv)]
# ids = sys.argv[2:len(sys.argv)]
ids = map(lambda x: int(x) - 1, ids)

w_range = int(img.width / 5)
h_range = int((img.height - YELLOW_OFFSET) / 6)

stacked = 0

for i, id in enumerate(ids):
    x = math.floor(id/6) * w_range + (math.floor(id/6) * 2)
    y = id % 6 * h_range + (id % 6 * 4)
    cropped = img.crop([x,y + YELLOW_OFFSET,x+w_range-5,y+h_range + YELLOW_OFFSET])
    if i != 0:
        stacked = Image.blend(stacked, cropped, pow(0.5, i))
    else:
        stacked = cropped

stacked.show()

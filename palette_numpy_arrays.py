from PIL import Image
import random
import sys
import numpy as np

size = int(sys.argv[1]) if len(sys.argv) > 1 else 5
final_scale = int(sys.argv[2]) if len(sys.argv) > 2 else 500

def to_hex(rgb):
	return '#' + ''.join('%02x'%i for i in rgb).upper()

def random_color():
	return np.random.randint(1,255,[3])

def gradient(start, end, steps):
	diff_r = ((end[0] - start[0]) / steps)
	diff_g = ((end[1] - start[1]) / steps)
	diff_b = ((end[2] - start[2]) / steps)
	colors = np.empty([1,size,3])
	colors[0,0] = start
	for i in range(1, steps - 1):
		colors[0,i,0] = int(start[0] + i * diff_r)
		colors[0,i,1] = int(start[1] + i * diff_g)
		colors[0,i,2] = int(start[2] + i * diff_b)
	colors[0,size - 1] = end
	return colors

upleft = random_color()
downleft = random_color()
upright = random_color()
downright = random_color()

output = np.zeros([size,size,3])
first_row = gradient(upleft, downleft, size)
last_row = gradient(upright, downright, size)

for i in range(0, size):
	top_color = first_row[0,i]
	bottom_color = last_row[0,i]
	output[i,0:] = gradient(top_color, bottom_color, size)
	
imgname = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
im = Image.new('RGB', (size, size))
im = Image.fromarray(np.uint8(output))

im = im.resize((final_scale, final_scale))
im.save('images/' + imgname + '.png')
print('Saved as: ' + imgname + '.png')
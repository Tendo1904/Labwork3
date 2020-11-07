import math
import os
from PIL import Image
import matplotlib.pyplot as plt
a = []
o = []
t = 0 
while t <= 12.56:
	x = 13*(math.cos(t)-math.cos(6.5*t)/6.5)
	y = 13*(math.sin(t)-math.sin(6.5*t)/6.5)
	a.append(x)
	o.append(y)
	t += 0.157
plt.plot(a,o, color = 'black', marker = 'o')
plt.title('Axis')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('task9f.png', dpi = 300, bbox_inches = 'tight')
file_in = "task9f.png"
img = Image.open(file_in)
file_out = "task9f.bmp"
img.save(file_out)
os.remove('task9f.png')

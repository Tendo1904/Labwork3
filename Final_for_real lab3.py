import math
abscissa = []
ordinate = []
step = 0
four_Pies = 12.56
move_to_centerX = 256
move_to_centerY = 256
while step <= four_Pies:
	x = 13 * (math.cos(step) - math.cos(6.5*step)/6.5)
	y = 13 * (math.sin(step) - math.sin(6.5*step)/6.5)
	abscissa.append(x)
	ordinate.append(y)
	step += 0.057
for i in range(len(abscissa)):
	abscissa[i] = round(abscissa[i]+move_to_centerX)
	ordinate[i] = round(ordinate[i]+move_to_centerY)
zero_field = [[0 for j in range(0,512)] for i in range(0,512)]
for i in range(len(abscissa)):
	zero_field[abscissa[i]][ordinate[i]] = 1
with open('IloveBMP.bmp', 'wb') as f:
	f.write(b'BM')
	f.write((154).to_bytes(4, byteorder='little'))
	for i in range(2):
		f.write((0).to_bytes(2, byteorder='little'))

	f.write((122).to_bytes(4, byteorder='little'))
	f.write((108).to_bytes(4, byteorder='little'))
	f.write((512).to_bytes(4, byteorder='little'))
	f.write((512).to_bytes(4, byteorder='little'))
	f.write((1).to_bytes(2, byteorder='little'))
	f.write((32).to_bytes(2, byteorder='little'))
	f.write((3).to_bytes(4, byteorder='little'))
	f.write((32).to_bytes(4, byteorder='little'))
	for i in range(2):
		f.write((2835).to_bytes(4, byteorder='little'))
		f.write((0).to_bytes(4, byteorder='little'))

	f.write(b'\x00\x00\xFF\x00')
	f.write(b'\x00\xFF\x00\x00')
	f.write(b'\xFF\x00\x00\x00')
	f.write(b'\x00\x00\x00\xFF')
	f.write(b' niW')
	f.write((0).to_bytes(36, byteorder='little'))
	for i in range(3):
		f.write((0).to_bytes(4, byteorder='little'))
	for i in range(0,512):
		for j in range(0,512):
			if zero_field[i][j]:
				f.write(b'\x00\x00\x00\xFF')
			else:
				f.write(b'\xFF\xFF\xFF\xFF')

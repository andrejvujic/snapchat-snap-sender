# snapchat-snap-sender
# git-hub: https://github.com/andrejvujic/snapchat-snap-sender
# NOTE: this was initially written for personal use so there are potential bugs

from ppadb.client import Client as AdbClient
from PIL import Image 
import numpy
import math

# Green Square color
R_1, G_1, B_1 = 122, 214, 131

# Blue Selected Friend color
R_2, G_2, B_2 = 20, 158, 230

# Create ADB connection
adb = AdbClient(host="127.0.0.1", port=5037)
# Get ADB devices
devices = adb.devices()

# Get first device (assume that is the user's device)
device = devices[0]

# Code to select all friends
def select():
	image = device.screencap()

	with open('screen.png', 'wb') as file:
		file.write(image)

	image = Image.open('screen.png')
	image = numpy.array(image, dtype = numpy.uint8)

	y = 195
	while y < 2200:
		pixel = list(image[y][186])[:3]

		pixel_r = pixel[0]
		pixel_g = pixel[1]
		pixel_b = pixel[2]

		distance_green = math.sqrt((R_1 - pixel_r) ** 2 + (G_1 - pixel_g) ** 2 +(B_1 - pixel_b) ** 2)

		if distance_green < 40:
			device.shell(f'input touchscreen tap {185} {y + 25} 50')
			print(f'tap at y=185 x={y + 25}.')
			y += 50

		else:
			y += 1

# Check if maximum scroll height has been reached
def check_scroll():
	image = device.screencap()

	with open('screen.png', 'wb') as file:
		file.write(image)

	image = Image.open('screen.png')
	image = numpy.array(image, dtype = numpy.uint8)

	y = 1925
	while y < 2100:

		pixel_selected = list(image[y][60])[:3]
		selected_r = pixel_selected[0]
		selected_g = pixel_selected[1]
		selected_b = pixel_selected[2]

		distance_blue = math.sqrt((R_2 - selected_r) ** 2 + (G_2 - selected_g) ** 2 + (B_2 - selected_b) ** 2)
		if distance_blue < 40:
			print(f'max. scroll height reached at y={y}.')
			send()
			
		y += 1

	print('max. scroll height not reached.')

def send():

	send_snap = input('Send snap? (y/n) ')
	
	if send_snap == "y":
		# Press send button
		device.shell('input touchscreen tap 995 2200 50')
		print('snap sent.')

	quit()

while True:
	select()
	# Swipe
	device.shell('input touchscreen swipe 100 2100 1080 200 5000')
	check_scroll()

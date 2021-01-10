# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/rainbow-2021-01-10-10-55-04.py"

from colorsys import hsv_to_rgb
from time import sleep
from sense_emu import SenseHat

sense = SenseHat()

r = (255, 0, 0)    #red
o = (255, 128, 0)  #orange
y = (255, 255, 0)  #yellow
g = (0, 255, 0)    #green
c = (0, 255, 255)  #cyan
b = (0, 0, 255)    #blue
p = (255, 0, 255)  #purple
n = (255, 128, 128)#pink
w = (255, 255, 255)#white
k = (0, 0, 0)      #blank

rainbow = [r,o,y,g,c,b,p,n]

heart = [
        k,r,r,k,k,r,r,k,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        k,r,r,r,r,r,r,k,
        k,k,r,r,r,r,k,k,
        k,k,k,r,r,k,k,k,
        ]

# Hues represent the spectrum of colors as values between 0 and 1. The range
# is circular so 0 represents red, ~0.2 is yellow, ~0.33 is green, 0.5 is cyan,
# ~0.66 is blue, ~0.84 is purple, and 1.0 is back to red. These are the initial
# hues for each pixel in the display.
hues = [
    0.00, 0.00, 0.06, 0.13, 0.20, 0.27, 0.34, 0.41,
    0.00, 0.06, 0.13, 0.21, 0.28, 0.35, 0.42, 0.49,
    0.07, 0.14, 0.21, 0.28, 0.35, 0.42, 0.50, 0.57,
    0.15, 0.22, 0.29, 0.36, 0.43, 0.50, 0.57, 0.64,
    0.22, 0.29, 0.36, 0.44, 0.51, 0.58, 0.65, 0.72,
    0.30, 0.37, 0.44, 0.51, 0.58, 0.66, 0.73, 0.80,
    0.38, 0.45, 0.52, 0.59, 0.66, 0.73, 0.80, 0.87,
    0.45, 0.52, 0.60, 0.67, 0.74, 0.81, 0.88, 0.95,
    ]

hat = SenseHat()

def scale(v):
    return int(v * 255)

while True:
    sense.clear()
    
    sense.show_message("THANK YOU", text_colour = w, back_colour = k)
    sleep(0.5)
    sense.show_message("NHS", text_colour = w, back_colour = b)
    sleep(0.5)
    sense.show_message("AND", text_colour = w, back_colour = k)
    sleep(0.5)
    sense.show_message("KEYWORKERS", text_colour = y, back_colour = p)
    sleep(1)
    for x in range(180):
        # Rotate the hues
        hues = [(h + 0.01) % 1.0 for h in hues]
        # Convert the hues to RGB values
        pixels = [hsv_to_rgb(h, 1.0, 1.0) for h in hues]
        # hsv_to_rgb returns 0..1 floats; convert to ints in the range 0..255
        pixels = [(scale(r), scale(g), scale(b)) for r, g, b in pixels]
        # Update the display
        hat.set_pixels(pixels)
        sleep(0.04)
    sleep(1)
    sense.show_message("STAY", text_colour = w, back_colour = k)
    sense.show_message("POSITIVE!", text_colour = w, back_colour = g)
    sleep(0.5)
    sense.show_message("TEST", text_colour = w, back_colour = k)
    sense.show_message("NEGATIVE!", text_colour = w, back_colour = r)
    sleep(0.5)
    
    sense.set_pixels(heart)
    sleep(3)
    
    for x in range(180):
        # Rotate the hues
        hues = [(h + 0.01) % 1.0 for h in hues]
        # Convert the hues to RGB values
        pixels = [hsv_to_rgb(h, 1.0, 1.0) for h in hues]
        # hsv_to_rgb returns 0..1 floats; convert to ints in the range 0..255
        pixels = [(scale(r), scale(g), scale(b)) for r, g, b in pixels]
        # Update the display
        hat.set_pixels(pixels)
        sleep(0.04)


    
from sense_hat import SenseHat
import time

sense = SenseHat()

sense.set_rotation(180)

b = (0, 160, 220)
g = (112, 192, 75)
e = (0, 0, 0)

logo = [
	e, e, b, b, b, b, e, e,
	e, b, e, e, e, e, b, e,
	b, e, e, b, b, e, e, b,
	b, e, g, g, g, g, e, b,
	b, e, e, g, g, e, e, b,
	b, e, g, e, e, g, e, b,
	e, b, e, e, e, e, b, e,
	e, e, b, b, b, b, e, e
]

sense.set_pixels(logo)

time.sleep(5)

sense.clear()

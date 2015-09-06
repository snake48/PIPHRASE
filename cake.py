import unicornhat as uh
import time
FRAMES = [
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]], [[255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
]
for x in FRAMES:
	 uh.set_pixels(x)
	 uh.show()
	 time.sleep(0.25)

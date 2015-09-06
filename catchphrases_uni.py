import time,random
import unicornhat as uh

cp_boat = [
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [255, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 255], [255, 0, 0], [255, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [255, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 255], [0, 0, 255], [255, 0, 0], [255, 0, 0], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [255, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 0, 0], [255, 0, 0], [0, 0, 255], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
[[[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[255, 255, 0], [255, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [255, 255, 255], [255, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 255]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0]], [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [0, 255, 0]]],
]


cp_weather = [
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 255], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 255, 0], [0, 255, 255], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 255], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 255], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [255, 255, 0], [255, 255, 0]], [[0, 0, 0], [102, 0, 204], [102, 0, 204], [102, 0, 204], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
]

cp_cake = [
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


cp_twowrongs = [
[[[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]]],
[[[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]]],
[[[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0]], [[255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]]],
[[[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]], [[0, 0, 0], [0, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0]], [[0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0]], [[0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]],
]

CATCHPHRASES= [cp_boat,cp_cake,cp_twowrongs, cp_weather]

'''ANSWERS = dict ((name, eval(name)) for name in ['cp_weather','cp_boat','cp_twowrongs','cp_cake'])'''

ANSWERS = {"Two wrongs don't make a right": cp_twowrongs, "When the boat comes in":cp_boat,"have your cake and eat it":cp_cake,"under the weather":cp_weather}
'''uh.rotation(90)
def show_catchphrase():
    picked = random.choice(ANSWERS.keys())
    for i in range(1):
        for x in ANSWERS[picked]:
           uh.set_pixels(x)
           uh.show()
           time.sleep(0.25)
        time.sleep(1)
    return picked

show_catchphrase()'''


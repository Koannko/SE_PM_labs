import simple_draw as sd
import random

sd.resolution = (1000, 600)
def draw_smile(x, y, color):
    centre = sd.get_point(x, y)
    sd.circle(center_position=centre, radius=50, color=color, width=50)
    sd.line(start_point=sd.get_point(x-10,y-25), end_point=sd.get_point(x+10, y-25), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x-30,y), end_point=sd.get_point(x+-20, y+20), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x-20,y+20), end_point=sd.get_point(x-10, y), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x+10,y), end_point=sd.get_point(x+20, y+20), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x+20,y+20), end_point=sd.get_point(x+30, y), color=sd.COLOR_BLACK, width=5)

for i in range(10):
    draw_smile(sd.random_number(100, 900), sd.random_number(100, 500), sd.random_color())
sd.pause()
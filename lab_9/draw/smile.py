import simple_draw as sd
import random

def draw_smile(x, y, color):
    centre = sd.get_point(x, y)
    sd.circle(center_position=centre, radius=10, color=color, width=10)
    sd.line(start_point=sd.get_point(x-2,y-5), end_point=sd.get_point(x+2, y-5), color=sd.COLOR_BLACK, width=2)
    sd.line(start_point=sd.get_point(x-6,y), end_point=sd.get_point(x+-4, y+4), color=sd.COLOR_BLACK, width=2)
    sd.line(start_point=sd.get_point(x-5,y+4), end_point=sd.get_point(x-2, y), color=sd.COLOR_BLACK, width=2)
    sd.line(start_point=sd.get_point(x+2,y), end_point=sd.get_point(x+4, y+4), color=sd.COLOR_BLACK, width=2)
    sd.line(start_point=sd.get_point(x+4,y+4), end_point=sd.get_point(x+6, y), color=sd.COLOR_BLACK, width=2)

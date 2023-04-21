import simple_draw as sd

def draw_wall(width=500, height=200):
    for j in range(10):
        for i in range(10):
            start = sd.get_point(width + i * 32 -j % 2 * 16, height + j * 15)
            end = sd.get_point(width + i * 32 + 25 + 5 - j % 2 * 16, height + j * 15 + 12)
            sd.rectangle(left_bottom=start, right_top=end, color=sd.COLOR_RED)
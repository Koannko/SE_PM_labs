import simple_draw as sd

def draw_wall(width=500, height=200):
    for j in range(10):
        for i in range(10):
            start = sd.get_point(width + i * 130 -j % 2 * 65, height + j * 60)
            end = sd.get_point(width + i * 130 + 100 + 20 - j % 2 * 65, height + j * 60 + 50)
            sd.rectangle(left_bottom=start, right_top=end, color=sd.COLOR_RED)
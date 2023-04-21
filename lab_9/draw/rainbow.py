import simple_draw as sd

def draw_rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                    sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    x1, y1, x2, y2 = 1500, 500, 2000, 1000
    width = 4
    for color_item in rainbow_colors:
        start_point = sd.get_point(x1, y1)
        end_point = sd.get_point(x2, y2)
        sd.line(start_point=start_point, end_point=end_point, color=color_item, width=width)
        x1 += 5
        x2 += 5

    x_center, y_center = 600, -100
    center_position = sd.get_point(x_center, y_center)
    radius = 400
    width = 10
    for color_item in rainbow_colors:
        sd.circle(center_position=center_position, radius=radius, color=color_item, width=width)
        radius -= -11
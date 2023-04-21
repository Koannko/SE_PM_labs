import simple_draw as sd

def draw_rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                    sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    
    x_center, y_center = 300, -50
    center_position = sd.get_point(x_center, y_center)
    radius = 750
    width = 10
    for color_item in rainbow_colors:
        sd.circle(center_position=center_position, radius=radius, color=color_item, width=width)
        radius -= -11
import simple_draw as sd

def draw_tree(start_point, start_angle, branch_length):
    if branch_length < 10:
        return
    start_point = sd.vector(start_point, start_angle, branch_length)
    
    alpha = 30 * sd.random_number(0, 40) / 100
    branch_length *= 0.75 * sd.random_number(0, 20) / 100    
    draw_tree(start_point, start_angle + alpha, branch_length)
    draw_tree(start_point, start_angle - alpha, branch_length)

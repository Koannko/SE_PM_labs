import simple_draw as sd

def snowflake_gen(width = 800, height = 800):
    return {'length': sd.random_number(10, 20),
            'x': width + sd.randint(-50, 50),
            'y': height + sd.randint(-50, 50),
            'factor_a': sd.random_number(4, 7) / 10,
            'factor_b': sd.random_number(4, 7) / 10,
            'factor_c': sd.random_number(45, 60)
            }

def draw_snowflake(width, height):
    snowflake = snowflake_gen(width, height)
    point = sd.get_point(snowflake['x'], snowflake['y'])
    sd.snowflake(
        point,
        snowflake['length'],
        sd.COLOR_WHITE,
        snowflake['factor_a'],
        snowflake['factor_b'],
        snowflake['factor_c'])

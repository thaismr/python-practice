from termcolor import colored
# After pip install termcolor at the Terminal tab

print()
print(colored('Procedural', 'red'), colored('Mini Game', 'green'), '\n')


# Init values
player_health = 0
player_location = (0, 0, 0)


def check_player_at_sight(location=(0, 0, 0), f_true=None, f_false=None):
    return f_true if location == player_location else f_false


def check_health(health, target_health, f_true=None, f_false=None):
    return f_true if health >= target_health else f_false


def hit_player(strength=0):
    global player_health
    player_health -= strength
    if player_health < 0:
        player_health = 0


def run_away(location=[0, 0, 0]):
    x, y, z = location
    if x < 10:
        x += 1
    elif y < 10:
        y += 1
    elif z < 10:
        z += 1
    else:
        x = 9
    location = [x, y, z]


def walk(location=[0, 0, 0]):
    x, y, z = location
    if x < 10:
        x += 1
        location = [x, y, z]
    else:
        location = [9, y, z]


behavior_tuple = (check_player_at_sight, check_health, hit_player, run_away)
print(type(behavior_tuple))

behavior_dict = {
    0: {
        'f': check_player_at_sight,
        True: {
            'f': check_health,
            True: {
                'f': hit_player
            },
            False: {
                'f': run_away
            }
        }
    }
}

gen_behavior = (f() for f in behavior_tuple)


def master_enemies(enemy):
    def slave_enemy(*args, **kwargs):
        result = enemy(*args, **kwargs)
        name = kwargs['name']
        color = kwargs['color']
        print(colored(name, color), 'General enemy functionality here...')
        return result
    return slave_enemy


@master_enemies
def easy_enemy(name, color='white'):
    speed = 1.0
    strength = 1.0
    max_health = 1.0
    name = colored(name, color)
    print(f'{name}: Easy enemy functionality here...')


@master_enemies
def strong_enemy(name, color='white'):
    speed = 5.0
    strength = 5.0
    max_health = 5.0
    name = colored(name, color)
    print(f'{name}: Strong enemy functionality here...')


easy_enemy(name='Easy enemy #1', color='blue')
easy_enemy(name='Easy enemy #2', color='green')
strong_enemy(name='Boss enemy', color='red')

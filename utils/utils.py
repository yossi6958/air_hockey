import re

import pygame

# Map key names to Pygame constants
KEY_MAP = {
    'UP': pygame.K_UP,
    'DOWN': pygame.K_DOWN,
    'LEFT': pygame.K_LEFT,
    'RIGHT': pygame.K_RIGHT,
    'SPACE': pygame.K_SPACE,
    'RETURN': pygame.K_RETURN,
    'ESCAPE': pygame.K_ESCAPE,
    # Add more mappings as needed
}


# Define a function to parse the configuration file
def parse_game_features(filename):
    game_features = {
        'WIDTH': None,
        'HEIGHT': None,
        'GOAL1_POSITION': None,
        'GOAL2_POSITION': None,
        'PADDLE_RADIUS': None,
        'PUCK_RADIUS': None,
        'PADDLE_SPEED': None,
        'player1_key': None,
        'player2_key': None,
        'M': None,
        'N': None
    }

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            if 'WIDTH' in line:
                game_features['WIDTH'] = int(re.search(r'(\d+)', line).group())
            elif 'HEIGHT' in line:
                game_features['HEIGHT'] = int(re.search(r'(\d+)', line).group())
            elif 'GOAL1 POSITION' in line:
                values = re.findall(r'\d+', line)
                game_features['GOAL1_POSITION'] = [(int(values[0]), int(values[1])), int(values[2])]
            elif 'GOAL2 POSITION' in line:
                values = re.findall(r'\d+', line)
                game_features['GOAL2_POSITION'] = [(int(values[0]), int(values[1])), int(values[2])]
            elif 'PADDLE_RADIUS' in line:
                game_features['PADDLE_RADIUS'] = int(re.search(r'(\d+)', line).group())
            elif 'PUCK_RADIUS' in line:
                game_features['PUCK_RADIUS'] = int(re.search(r'(\d+)', line).group())
            elif 'PADDLE_SPEED' in line:
                game_features['PADDLE_SPEED'] = int(re.search(r'(\d+)', line).group())
            elif 'player1_key' in line:
                key_names = re.findall(r'pygame\.K_(\w+)', line)
                game_features['player1_key'] = [KEY_MAP.get(name, None) for name in key_names]
            elif 'player2_key' in line:
                # Assuming mouse control for player2, set a placeholder
                game_features['player2_key'] = 'mouse'
            elif 'M' in line:
                game_features['M'] = int(re.search(r'(\d+)', line).group())
            elif 'N' in line:
                game_features['N'] = int(re.search(r'(\d+)', line).group())

    return game_features


if __name__ == '__main__':
    game_features = parse_game_features('game_features.txt')
    print(game_features)

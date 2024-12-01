MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def parse_game(game_str):
    game_id, pulls = game_str.split(": ")
    game_id = int(game_id.split(" ")[1])
    pulls = pulls.split("; ")
    
    parsed_pulls = []
    for pull in pulls:
        counts = {"red": 0, "green": 0, "blue": 0}
        items = pull.split(", ")
        for item in items:
            num, color = item.split(" ")
            counts[color] = int(num)
        parsed_pulls.append(counts)
    return game_id, parsed_pulls

def calculate_minimum_power(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    total_power = 0

    for line in lines:
        game_id, pulls = parse_game(line.strip())
        
        min_red = 0
        min_green = 0
        min_blue = 0

        for pull in pulls:
            min_red = max(min_red, pull["red"])
            min_green = max(min_green, pull["green"])
            min_blue = max(min_blue, pull["blue"])

        power = min_red * min_green * min_blue
        total_power += power

    return total_power

if __name__ == "__main__":
    file_path = "Day2_input.txt"
    result = calculate_minimum_power(file_path)
    print(f"Sum of the power of minimum sets: {result}")
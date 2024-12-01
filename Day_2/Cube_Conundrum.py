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

def is_game_possible(pulls):
    for pull in pulls:
        if pull["red"] > MAX_RED or pull["green"] > MAX_GREEN or pull["blue"] > MAX_BLUE:
            return False
    return True

def calculate_possible_game_ids(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    possible_game_ids = []
    for line in lines:
        game_id, pulls = parse_game(line.strip())
        if is_game_possible(pulls):
            possible_game_ids.append(game_id)

    return sum(possible_game_ids)

if __name__ == "__main__":
    file_path = "Day2_input.txt"
    result = calculate_possible_game_ids(file_path)
    print(f"Sum of possible game IDs: {result}")

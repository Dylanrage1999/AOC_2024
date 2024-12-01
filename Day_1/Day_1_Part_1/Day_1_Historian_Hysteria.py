def calculate_distance_from_vertical_file(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    total_distance = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))
    
    return total_distance

file_path = 'day1_input.txt'

total_distance = calculate_distance_from_vertical_file(file_path)
print(f"Total distance: {total_distance}")
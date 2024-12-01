from collections import Counter

def calculate_similarity_score(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    right_count = Counter(right_list)

    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count.get(num, 0)

    return similarity_score

file_path = '../Day_1_Part_1/day1_input.txt'

similarity_score = calculate_similarity_score(file_path)
print(f"Similarity score: {similarity_score}")
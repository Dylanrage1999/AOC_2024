word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def get_combined_digits(line):
    positions = [
        (idx, digit)
        for word, digit in word_to_digit.items()
        for idx in range(len(line))
        if line.startswith(word, idx)
    ]
    positions.extend((idx, ch) for idx, ch in enumerate(line) if ch.isdigit())
    if not positions:
        return 0
    positions.sort(key=lambda x: x[0])
    first, last = positions[0][1], positions[-1][1]
    return int(first + last)

def sum_calibration_values(lines):
    total = 0
    for line in lines:
        tmp = get_combined_digits(line.strip())
        total += tmp
    return total

def main():
    with open("Day1_input.txt") as f:
        lines = f.readlines()
        print(sum_calibration_values(lines))

if __name__ == "__main__":
    main()
def calculate_calibration_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            first_digit = None
            last_digit = None
            
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break

            if first_digit and last_digit:
                calibration_value = int(first_digit + last_digit)
                total_sum += calibration_value
    
    return total_sum

file_path = 'Day1_input.txt'
result = calculate_calibration_sum(file_path)
print(f"The sum of all calibration values is: {result}")
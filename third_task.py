def read_file():
    with open("./data/third_task.txt", encoding="utf-8") as file:
        return [line.strip().split() for line in file.readlines()]

def replace_na_with_average(row):
    # Преобразуем все числа в int, игнорируя N/A
    row = [int(x) if x != "N/A" else None for x in row]
    for i, value in enumerate(row):
        if value is None:
            left = row[i - 1] if i > 0 else 0
            right = row[i + 1] if i < len(row) - 1 else 0
            row[i] = (left + right) // 2
    return row

def filter_negative_odd_numbers(row):
    return [x for x in row if x < 0 and x % 2 != 0]

def calculate_average(row):
    return sum(row) / len(row) if row else 0

def process_data(data):
    averages = []
    for row in data:
        replaced_row = replace_na_with_average(row)
        filtered_row = filter_negative_odd_numbers(replaced_row)
        average = calculate_average(filtered_row)
        averages.append(average)
    return averages

def write_averages_to_file(averages):
    with open("third_task_result.txt", "w", encoding="utf-8") as file:
        for avg in averages:
            file.write(f"{avg:.2f}\n")

data = read_file()
averages = process_data(data)
write_averages_to_file(averages)

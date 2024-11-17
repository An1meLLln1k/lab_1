def read_file():
    with open("./data/fourth_task.txt", encoding="utf-8") as file:
        header = file.readline().strip().split(",")
        data = [line.strip().split(",") for line in file.readlines()]
        return header, data

def remove_column(header, data, column_name):
    if column_name in header:
        index = header.index(column_name)
        header.pop(index)
        for row in data:
            row.pop(index)
    return header, data

def calculate_mean(data, column_name, header):
    if column_name in header:
        index = header.index(column_name)
        values = []
        for row in data:
            try:
                values.append(float(row[index]))
            except ValueError:
                continue
        return sum(values) / len(values) if values else 0
    return None

def find_max_min(data, column_name, header):
    if column_name in header:
        index = header.index(column_name)
        values = []
        for row in data:
            try:
                values.append(int(row[index]))
            except ValueError:
                continue
        return max(values), min(values)
    return None, None

def filter_rows(data, column_name, header, excluded_value):
    if column_name in header:
        index = header.index(column_name)
        return [row for row in data if row[index] != excluded_value]
    return data

def write_results(mean_price, max_quantity, min_quantity, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Mean Price: {mean_price:.2f}\n")
        file.write(f"Max Quantity: {max_quantity}\n")
        file.write(f"Min Quantity: {min_quantity}\n")

def write_csv(header, data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(",".join(header) + "\n")
        for row in data:
            file.write(",".join(row) + "\n")


header, data = read_file()

header, data = remove_column(header, data, "rating")

mean_price = calculate_mean(data, "price", header)

max_quantity, min_quantity = find_max_min(data, "quantity", header)

filtered_data = filter_rows(data, "status", header, "In")

write_results(mean_price, max_quantity, min_quantity, "./data/fourth_task_result.txt")
write_csv(header, filtered_data, "./data/fourth_task_modified.csv")

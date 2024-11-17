def read_file():
    with open("./data/second_task.txt", encoding="utf-8") as file:
        return [list(map(int, line.strip().split())) for line in file.readlines()]
def process_line(line):
    return sum(abs(num) for num in line if num ** 2 < 100000)

def process_column(results):
    average = sum(results) / len(results) if results else 0
    return results, average

def write_results(results, average):
    with open("second_task_result.txt", "w", encoding="utf-8") as file:
        for result in results:
            file.write(f"{result}\n")
        file.write(f"Среднее арифметическое: {average:.2f}\n")

lines = read_file()
results = [process_line(line) for line in lines]
column, average = process_column(results)
write_results(column, average)
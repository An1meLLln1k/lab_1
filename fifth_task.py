import csv
from bs4 import BeautifulSoup

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return BeautifulSoup(content, 'html.parser')

def extract_table_data(soup):
    table = soup.find('table')
    if not table:
        raise ValueError("Таблица не найдена в HTML-файле.")
    headers = [th.text.strip() for th in table.find('thead').find_all('th')]
    rows = [
        [td.text.strip() for td in row.find_all('td')]
        for row in table.find('tbody').find_all('tr')
    ]
    return headers, rows

def save_to_csv(headers, rows, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

def main():
    html_path = './data/fifth_task.html'
    csv_path = 'fifth_task_result.csv'
    soup = read_html_file(html_path)
    headers, rows = extract_table_data(soup)
    save_to_csv(headers, rows, csv_path)
    print(f'Данные успешно извлечены и сохранены в файл {csv_path}')

if __name__ == '__main__':
    main()

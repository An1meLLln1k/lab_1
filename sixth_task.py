import requests
from bs4 import BeautifulSoup


def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Ошибка при получении данных: {response.status_code}")


def convert_json_to_html(data):
    html = '<html><head><title>Users</title></head><body>'
    html += '<table border="1">'
    html += '<tr>'

    headers = data[0].keys()
    for header in headers:
        html += f'<th>{header}</th>'
    html += '</tr>'

    for item in data:
        html += '<tr>'
        for key in headers:
            html += f'<td>{item[key]}</td>'
        html += '</tr>'

    html += '</table>'
    html += '</body></html>'
    return html


def save_html_to_file(html, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html)


def main():
    api_url = "https://jsonplaceholder.typicode.com/users"
    html_path = "./data/sixths_task_result.html"

    data = fetch_data_from_api(api_url)
    html = convert_json_to_html(data)
    save_html_to_file(html, html_path)
    print(f"Данные успешно сохранены в файл {html_path}")


if __name__ == "__main__":
    main()

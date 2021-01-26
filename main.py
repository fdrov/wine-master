from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import pandas as pd
import collections


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')

# вычисляме количество лет со дня открытия винодельни
company_age = ((datetime.today() - datetime(year=1920, month=12, day=31)).days) // 365

# получаем вина по сортам их файла wine2
wine_data_frame = pd.read_excel(r".\wine3.xlsx", keep_default_na=False)
wine_dict = wine_data_frame.to_dict(orient='records')

# форматируем словарь в список словарей для использования в template.html
wine_list_for_template = collections.defaultdict(list)
for bottle in wine_dict:
    wine_list_for_template[bottle['Категория']].append(bottle)


rendered_page = template.render(how_old=company_age,
                                wines=wine_list_for_template)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
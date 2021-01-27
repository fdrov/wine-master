from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd
import collections
import dotenv

config = dotenv.dotenv_values('.env')


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html']),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template('template.html')

# вычисляем возраст винодельни
today = datetime.date.today().year
foundation_year = 1920
company_age = today - foundation_year

last_digit = company_age % 10
if last_digit == 1 and company_age != 11:
    company_age_years = f'{company_age} год'
elif last_digit in (2, 3, 4) and (company_age < 12 or company_age > 19):
    company_age_years = f'{company_age} года'
else:
    company_age_years = f'{company_age} лет'

# получаем вина по сортам их файла wine2
wine_data_frame = pd.read_excel(config['PATH_TO_EXCEL'], keep_default_na=False)
wine_dict = wine_data_frame.to_dict(orient='records')

# форматируем словарь в список словарей для использования в template.html
wine_list_for_template = collections.defaultdict(list)
for bottle in wine_dict:
    wine_list_for_template[bottle['Категория']].append(bottle)


rendered_page = template.render(company_age_years=company_age_years,
                                wines=wine_list_for_template)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
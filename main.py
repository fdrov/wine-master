from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import pandas as pd
import collections


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')

#вычисляме количество лет со дня открытия винодельни
how_old = ((datetime.today() - datetime(year=1920, month=12, day=31)).days) // 365

#получаем список вин из эксель файла
df = pd.read_excel(r"C:\Users\Maddy\Documents\TRASHBOX\wine.xlsx", keep_default_na=False).to_dict(orient='records')

#получаем вина по сортам их файла wine2
df = pd.read_excel(r"C:\Users\Maddy\Documents\TRASHBOX\wine3.xlsx", keep_default_na=False)
wine_dict = df.to_dict(orient='records')
wine2 = collections.defaultdict(list)
for i in wine_dict:
    wine2[i['Категория']].append(i)
wine2 = collections.UserDict(wine2)

rendered_page = template.render(how_old=how_old,
                                wines=wine2)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

# server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
# server.serve_forever()

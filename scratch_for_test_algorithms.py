import pandas as pd
import collections
import pprint

wine_data_frame = pd.read_excel(r".\wine3.xlsx", keep_default_na=False)

wine_dict = wine_data_frame.to_dict(orient='records')

wine_list_for_template = collections.defaultdict(list)

for i in wine_dict:
    wine_list_for_template[i['Категория']].append(i)

print(wine_list_for_template)

# wine_list_for_template = collections.UserDict(wine_list_for_template)

print(wine_list_for_template)

for wine_sort in wine_list_for_template:
    print(wine_list_for_template[wine_sort])

# for sort in wine_list_for_template:
#     print(wine_list_for_template[sort])
#     for bottle in wine_list_for_template[sort]:
#         print(bottle['Акция'])


## Группировка по сортам вин эксель файлавстроенным методом группировки пандас
# grouped = df.groupby(['Категория'])
#
# wine2 = {}
# for name, group in grouped:
#     wine2[name] = group.to_dict(orient='records')
# pprint.PrettyPrinter(sort_dicts=True).pprint(wine2)







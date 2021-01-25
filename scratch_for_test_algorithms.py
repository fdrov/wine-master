import pandas as pd
import collections
import pprint

df = pd.read_excel(r"C:\Users\Maddy\Documents\TRASHBOX\wine3.xlsx", keep_default_na=False)
# df = pd.read_csv('titanic.csv')

wine_dict = df.to_dict(orient='records')

wine2 = collections.defaultdict(list)

for i in wine_dict:
    wine2[i['Категория']].append(i)



wine2 = collections.UserDict(wine2)

# print(wine2)

for sort in wine2:
    print(wine2[sort])
    for bottle in wine2[sort]:
        print(bottle['Акция'])





# grouped = df.groupby(['Категория'])
#
# wine2 = {}
# for name, group in grouped:
#     wine2[name] = group.to_dict(orient='records')
# pprint.PrettyPrinter(sort_dicts=True).pprint(wine2)







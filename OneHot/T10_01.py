import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

x = set(data['whoAmI'])
out = pd.DataFrame() #data
# out = data    #Раскомментировать для проверки результата
for i in x:
    out[i] = [(1 if el == i else 0) for el in data['whoAmI']]
print(out)
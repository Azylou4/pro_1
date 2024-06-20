import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np

# Загружаем файл с данными
data = pd.read_csv("1.csv", encoding = "cp1251", sep=";")

# Убираем лишние регионы
data = data[data.REGION_NAME != "Республика Татарстан"]
data = data[data.REGION_NAME != "Республика Марий Эл" ]
print(data.count())

### Задание 1.1 ###
# Сортируем данные по столбцу 'SALARY'
sorted_data = data.sort_values(by=['SALARY'], ascending=True)
salaries = sorted_data['SALARY'].tolist()
print("Вариационный ряд:")
print(salaries)

### Задание 1.2 ###
mean = (sum(salaries) / len(salaries))
print("Выборочное среднее:", mean)
s2n = sum((i-mean)**2 for i in salaries)/len(salaries)
print("Смещенная выборочная дисперсия:", s2n)
s2 = len(salaries) * s2n / (len(salaries) - 1)
print("Несмещенная выборочная дисперсия:", s2)
print("Выборочная медиана:", statistics.median(salaries))

### Задание 1.3 ###
# Разбиваем данные на 10 интервалов
num_bins = 10
hist, bins = np.histogram(salaries, bins=num_bins)

# Вычисляем ширину интервала
bin_width = bins[1] - bins[0]

# Создаем гистограмму
plt.bar(bins[:-1], hist, width=bin_width, edgecolor='black')

# Добавляем количество вхождений в каждый интервал
for i in range(len(hist)):
    plt.text(bins[i], hist[i] + 10, str(hist[i]), ha='center', va='bottom')

# Добавляем подписи к осям и заголовок
plt.xlabel('Значение')
plt.ylabel('Кол-во вхождений')
plt.title('Гистограмма распределения')

# Отображаем гистограмму
plt.show()

print("Кол-во значений в интервале A(2):",hist[1])
print("Кол-во значений в интервале A(4):",hist[3])
print("Кол-во значений в интервале A(6):",hist[5])

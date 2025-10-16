# Гистограмма

## `plt.hist()`

Для построения гистограммы можно воспользоваться функцией [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html) из модуля `pyplot`. В параметре `bins` указывается количество интервалов, на которое нужно разбить диапазон значений. Функция рисует диаграмму и при этом возвращает кортеж из трех элементов:
- значения частот для каждого интервала;
- последовательность значений, соответствующих границам интервалов;
- специфический объект использованный для отрисовки гистограммы.

```python
lognormal_sample = np.random.lognormal(mean=0., 
									   sigma=0.5,
									   size=10000)
hist, bins, _ = plt.hist(lognormal_sample, bins=24, width=.2)
print(hist[:4], bins[:4])
print(len(hist), len(bins))
plt.show()
```

## `np.histogram()`

Другой вариант, получить значения гистограммы функцией [`histogram()`](https://numpy.org/doc/2.0/reference/generated/numpy.histogram.html) из библиотеки NumPy, затем визуализировать гистограмму функцией `bar()` из модуля `pyplot`, которая рисует столбчатые диаграммы.

```python
hist, bins = np.histogram(lognormal_sample, bins=24)
plt.bar(bins[:-1], hist, width=.20, 
		color='green', label="Histogram")
print(hist[:4], bins[:4])
plt.show()
```


Для [[Discrete Random Variable|дискретных случайных величин]] $X$ и $Y$, **условная функция вероятностей** (*conditional probability mass function* – Conditional PMF) $X$ при условии $Y = y$ определяется как:

$$
p_{X|Y}(x|y) = P(X = x | Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)}
$$

при условии, что $P(Y = y) > 0$.

- $P(X = x, Y = y) = p_{X,Y}(x,y)$ – [[Joint PMF|совместная функция вероятностей]]
- $P(Y = y) = p_Y(y)$ – [[Marginal PMF|маргинальная функция вероятностей]] случайной величины $Y$

Свойство нормировки: 

$$
\sum_{x} p_{X|Y}(x|y) = 1
$$

[[Conditional PDF|❐]] Условная плотность распределения

[[Conditional CDF|❐]] Условная функция распределения

[[Conditional Probabilities of Events|❐]] Условная вероятность события
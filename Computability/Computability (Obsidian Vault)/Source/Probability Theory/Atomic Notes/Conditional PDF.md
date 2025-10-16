
Для [[Continuous Random Variable|непрерывных случайных величин]] $X$ и $Y$ с [[Conditional PDF|совместной плотностью]] $f_{X,Y}(x,y)$, **условная плотность** (*conditional probability density function* – Conditional PDF) $X$ при условии $Y = y$ определяется как:

$$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$$

при условии, что $f_Y(y) > 0$, где:

- $f_{X,Y}(x,y)$ – [[Joint PDF|совместная плотность]]
- $f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dx$ – [[Marginal PDF|маргинальная плотность]] случайной величины $Y$

Свойство нормировки: 

$$
\int_{-\infty}^{\infty} f_{X|Y}(x|y) , dx = 1
$$

Для малого $\Delta x$: 

$$
P(x < X \leq x + \Delta x | Y = y) \approx f_{X|Y}(x|y) \cdot \Delta x
$$

[[Conditional PMF|❐]] Условная функция вероятностей

[[Conditional CDF|❐]] Условная функция распределения

[[Conditional Probabilities of Events|❐]] Условная вероятность события
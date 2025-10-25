
Пусть $X$ и $Y$ – [[Random Variable|случайные величины]] на [[Probability Space|вероятностном пространстве]] $(\Omega, \mathcal{F}, P)$. **Условная функция распределения** (*conditional cumulative distribution function* – Conditional CDF) $X$ при условии $Y = y$ определяется как:

$$
F_{X|Y}(x|y) = P(X \leq x | Y = y)
$$

Для дискретного случая: 

$$
F_{X|Y}(x|y) = \sum_{t \leq x} P(X = t | Y = y)
$$

Для непрерывного случая: 

$$
F_{X|Y}(x|y) = \int_{-\infty}^{x} f_{X|Y}(t|y) , dt
$$

где $f_{X|Y}$ – [[Conditional PDF|условная плотность]].

[[Conditional PDF|❐]] Условная плотность распределения

[[Conditional PMF|❐]] Условная функция вероятностей

[[Conditional Probabilities of Events|❐]] Условная вероятность события

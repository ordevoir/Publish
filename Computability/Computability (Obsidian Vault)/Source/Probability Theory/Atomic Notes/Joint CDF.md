
**Совместной функцией распределения** (_Joint Cumulative Distribution Function_ – Joint CDF) [[Random Variable|случайных величин]] $X$ и $Y$ называется функция $F_{X,Y}: \mathbb{R}^2 \to [0,1]$, определяющая вероятность того, что одновременно $X < x$ и $Y < y$:

$$F_{X,Y}(x,y) = P(X < x, Y < y)$$

или более формально:

$$F_{X,Y}(x,y) = P({\omega \in \Omega : X(\omega) < x \text{ и } Y(\omega) < y})$$

где $\Omega$ – пространство элементарных исходов [[Probability Space|❐]].

Для $n$ случайных величин $X_1, X_2, \ldots, X_n$ совместная функция распределения определяется как:

$$F_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = P(X_1 < x_1, \ldots, X_n < x_n)$$

Совместная функция распределения [[Continuous Random Variable|непрерывной случайной величины]] выражается через [[Joint PDF|совместную плотность]] $f_{X,Y}(s,t)$:

$$F_{X,Y}(x,y) = \int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(s,t) , dt , ds$$

Совместная функция распределения [[Discrete Random Variable|дискретной случайной]] величины вырежется через совместную [[Joint PMF|функцию вероятности]] $p_{X,Y}(x_i,y_j)$:

$$
F_{X,Y}(x,y) = \sum_{x_i \le x}\;\sum_{y_j \le y} p_{X,Y}(x_i,y_j)
$$

[[Joint PDF|❐]] Совместная плотность вероятности

[[Joint PMF|❐]] Совместная функция вероятности
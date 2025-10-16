
**Совместной плотностью вероятности** (_Joint Probability Density Function_ – Joint PDF) [[Continuous Random Variable|непрерывных случайных величин]] $X$ и $Y$ называется функция $f_{X,Y}: \mathbb{R}^2 \to [0,\infty)$, такая что для любой области $B \subseteq \mathbb{R}^2$:

$$
P((X,Y) \in B) = \iint_B f_{X,Y}(x,y) , dx , dy
$$

Для $n$ непрерывных случайных величин совместная плотность определяется аналогично:

$$
P((X_1,\ldots,X_n) \in B) = \int_B f_{X_1,\ldots,X_n}(x_1,\ldots,x_n) , dx_1 \cdots dx_n
$$

Свойства:

- $f_{X,Y}(x,y) \geq 0$ для всех $(x,y)$
- $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x,y) , dx , dy = 1$

[[Joint CDF|❐]] Совместная функция распределения

[[Joint PMF|❐]] Совместная функция вероятности
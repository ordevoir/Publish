
**Вырожденная** (*degenerate*) или константная случайная величина – это случайная величина, которая принимает единственное возможное значение $c$ с вероятностью $1$:

$$
\mathbb P\{X=c\}=1
$$

[[Cumulative Distribution Function CDF|Функция распределения]]:

$$
F_X(x)=
\begin{cases}
0, & x<c,\\
1, & x\ge c.
\end{cases}
$$

Если рассматривать как [[Discrete Random Variable|дискретную случайную величины]], то [[Probability Mass Function PMF|функция вероятности]] PMF принимает значение $1$ в единственной точке $c$:

$$
p(c)=1
$$

Если рассматривать как [[Continuous Random Variable|непрерывную случайную величину]], то [[Probability Density Function PDF|плотности вероятности]] PDF может быть выражена через дельта-функцию Дирака: 

$$
f(x)=\delta(x-c)
$$

[[Expected Value|Математическое ожидание]] $\mathbb E[X]=c$

[[Variance|Дисперсия]] $\operatorname{Var}(X)=0$ (все высшие [[Central Moments|центральные моменты]] тоже 0).


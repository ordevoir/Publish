

**Абсолютный момент** (*absolute moment*) порядка $k$ случайной величины $X$:

$$
\alpha_k=\mathbb E\!\left[\,|X|^k\,\right]\quad (k>0),
$$

**Центральный абсолютный момент** (*central absolute moment*):

$$
\alpha_k^{(c)}=\mathbb E\!\left[\,|X-\mu|^k\,\right],\quad \mu=\mathbb E X.
$$

[[Discrete Random Variable|Дискретный случай]]: $\displaystyle \sum_x |x|^k\,P\{X=x\}$.

[[Continuous Random Variable|Непрерывный случай]]: $\displaystyle \int_{-\infty}^{\infty} |x|^k f(x)\,dx$.


>[!addition] Выборочные оценки
Для данных $x_1,\dots,x_n$:
> $$
> \hat\alpha_k=\frac1n\sum_{i=1}^n |x_i|^k,\qquad 
> \hat\alpha_k^{(c)}=\frac1n\sum_{i=1}^n |x_i-\bar x|^k.
> $$
> Они состоятельны при существовании соответствующего момента.


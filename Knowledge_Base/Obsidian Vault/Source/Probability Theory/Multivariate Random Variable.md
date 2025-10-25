## Многомерная случайная величина (Multivariate Random Variable)

**Определение:** Пусть $(\Omega, \mathcal{F}, P)$ — вероятностное пространство. $n$-мерная случайная величина (или случайный вектор) — это измеримое отображение: $$\mathbf{X}: \Omega \rightarrow \mathbb{R}^n$$ $$\mathbf{X}(\omega) = (X_1(\omega), X_2(\omega), \ldots, X_n(\omega))^T$$

где каждая компонента $X_i: \Omega \rightarrow \mathbb{R}$ является (одномерной) случайной величиной.

Измеримость означает, что для любого борелевского множества $B \in \mathcal{B}(\mathbb{R}^n)$: $$\mathbf{X}^{-1}(B) = {\omega \in \Omega : \mathbf{X}(\omega) \in B} \in \mathcal{F}$$

## Основные понятия

### 1. Совместная функция распределения (Joint Distribution Function)

**Определение:** Совместная функция распределения случайного вектора $\mathbf{X} = (X_1, \ldots, X_n)^T$: $$F_{\mathbf{X}}(x_1, \ldots, x_n) = P(X_1 \leq x_1, \ldots, X_n \leq x_n) = P(\bigcap_{i=1}^n {X_i \leq x_i})$$

### 2. Маргинальные распределения (Marginal Distributions)

**Определение:** Маргинальная функция распределения $i$-й компоненты: $$F_{X_i}(x_i) = \lim_{x_j \to +\infty, j \neq i} F_{\mathbf{X}}(x_1, \ldots, x_n)$$

Для подвектора $\mathbf{X}_I = (X_{i_1}, \ldots, X_{i_k})^T$, где $I = {i_1, \ldots, i_k} \subseteq {1, \ldots, n}$: $$F_{\mathbf{X}_I}(x_{i_1}, \ldots, x_{i_k}) = \lim_{x_j \to +\infty, j \notin I} F_{\mathbf{X}}(x_1, \ldots, x_n)$$

### 3. Условные распределения (Conditional Distributions)

Для дискретного случая, условная вероятностная функция (conditional probability mass function): $$p_{X|Y}(x|y) = \frac{P(X = x, Y = y)}{P(Y = y)}, \quad \text{при } P(Y = y) > 0$$

Для непрерывного случая с плотностью, условная плотность (conditional density): $$f_{X|Y}(x|y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}, \quad \text{при } f_Y(y) > 0$$

## Основные характеристики

### 1. Вектор математических ожиданий (Mean Vector)

**Определение:** Для случайного вектора $\mathbf{X} = (X_1, \ldots, X_n)^T$: $$\boldsymbol{\mu} = E[\mathbf{X}] = (E[X_1], \ldots, E[X_n])^T$$ где $E[X_i] = \int_{\mathbb{R}} x_i , dF_{X_i}(x_i)$

### 2. Ковариационная матрица (Covariance Matrix)

**Определение:** Ковариационная матрица $\boldsymbol{\Sigma}$ — это $n \times n$ матрица с элементами: $$\Sigma_{ij} = \text{Cov}(X_i, X_j) = E[(X_i - \mu_i)(X_j - \mu_j)]$$

В матричной форме: $$\boldsymbol{\Sigma} = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]$$

**Свойства:**

- $\boldsymbol{\Sigma}$ — симметричная матрица: $\Sigma_{ij} = \Sigma_{ji}$
- $\boldsymbol{\Sigma}$ — неотрицательно определённая: $\mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a} \geq 0$ для любого $\mathbf{a} \in \mathbb{R}^n$
- Диагональные элементы: $\Sigma_{ii} = \text{Var}(X_i) = \sigma_i^2$

### 3. Корреляционная матрица (Correlation Matrix)

**Определение:** Корреляционная матрица $\mathbf{R}$ с элементами: $$R_{ij} = \rho_{ij} = \frac{\text{Cov}(X_i, X_j)}{\sqrt{\text{Var}(X_i)\text{Var}(X_j)}} = \frac{\Sigma_{ij}}{\sigma_i \sigma_j}$$

где $\rho_{ij}$ — коэффициент корреляции Пирсона (Pearson correlation coefficient).

**Свойства:**

- $-1 \leq \rho_{ij} \leq 1$
- $\rho_{ii} = 1$
- $\rho_{ij} = \rho_{ji}$

### 4. Независимость (Independence)

**Определение:** Случайные величины $X_1, \ldots, X_n$ называются независимыми (independent), если: $$F_{\mathbf{X}}(x_1, \ldots, x_n) = \prod_{i=1}^n F_{X_i}(x_i) \quad \forall (x_1, \ldots, x_n) \in \mathbb{R}^n$$

**Следствия независимости:**

- Для независимых $X_i, X_j$: $\text{Cov}(X_i, X_j) = 0$ (обратное неверно)
- Для независимых $X_1, \ldots, X_n$: $E[\prod_{i=1}^n X_i] = \prod_{i=1}^n E[X_i]$

### 5. Характеристическая функция (Characteristic Function)

**Определение:** Характеристическая функция случайного вектора $\mathbf{X}$: $$\varphi_{\mathbf{X}}(\mathbf{t}) = E[e^{i\mathbf{t}^T\mathbf{X}}] = E[\exp(i\sum_{j=1}^n t_j X_j)]$$ где $\mathbf{t} = (t_1, \ldots, t_n)^T \in \mathbb{R}^n$, $i = \sqrt{-1}$.

**Свойство:** Характеристическая функция однозначно определяет распределение случайного вектора.
# Draft

Случайная величина называется **одномерной**, если возможные значения определяются одним числом. Значения **многомерной** СВ определяются несколькими числами. Частным случаем являются двумерные СВ.


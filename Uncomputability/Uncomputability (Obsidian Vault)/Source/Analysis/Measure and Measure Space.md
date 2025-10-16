
Пусть $(X, \mathcal{E})$ – [[Measurable Space and Sets|измеримое пространство]], где $X$ – непустое множество, а $\mathcal{E}⊆\mathcal{P}(X)$ – [[Sigma-Algebra|σ-алгебра подмножеств]] $X$. **Мерой** (*measure*) называется функция $μ: \mathcal{E} → [0, +∞]$, удовлетворяющая аксиомам:
- $μ(E)≥0$ для всех $E∈\mathcal{E}$ – неотрицательность;
- $μ(\varnothing) = 0$;
- **счетная аддитивность** (*countable additivity*) или **σ-аддитивность** (*σ-additivity*): для любой счетной [[Collection and Set|системы]] попарно непересекающихся множеств ${E_k}_{k=1}^∞⊆ \mathcal{E}$ выполняется   
$$
\mu\!\Bigl(\bigcup_{k=1}^\infty E_k\Bigr) = \sum_{k=1}^\infty \mu(E_k)
$$

Тройка $(X, \mathcal{E}, μ)$ называется **пространством с мерой** (*measure space*).

Мера $μ$ называется [[Probability Space|вероятностной]], если $μ(X)=1$.

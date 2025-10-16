
Пусть $(\Omega, \mathcal{F})$ – [[Measurable Space and Sets|измеримое пространство]], где $\Omega$ – непустое множество [[Probability Space|❐]], а $\mathcal{F}$ – [[Sigma-Algebra|σ-алгебра подмножеств]] $\Omega$.

**Вероятностную [[Measure and Measure Space|меру]]** (*probability measure*) $P: \mathcal{F} → [0, 1]$ можно определить через аксиомы Колмогорова:
- $P(A)≥0$ для всех $A∈\mathcal{F}$  – неотрицательность;
- $P(\Omega)=1$ – нормировка;
- **счетная аддитивность** (*countable additivity*) или **σ-аддитивность** (*σ-additivity*): для любой счетной [[Collection and Set|системы]] попарно непересекающихся множеств ${A_k}_{k=1}^∞⊆ \mathcal{F}$ выполняется   
$$
P\left(\bigcup_{k=1}^\infty A_k\right) =  \sum_{k=1}^\infty P(A_k)
$$

>[!addition]+ Следствия
> Из аксиом Колмогорова вытекают другие важные свойства вероятностной меры:
> - Из этих аксиом следует $P(\varnothing)=0$, поэтому, функция, удовлетворяющая аксиомам Колмогорова, удовлетворяет также и [[Measure and Measure Space|аксиомам меры]].
> - $P(A^c) = 1 - P(A)$ для дополнения $A^c=\Omega \setminus A$.
> - Если $A \subseteq B$, то $P(A) \leq P(B)$ (монотонность).
> - $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ (формула включений-исключений).
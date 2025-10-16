
Вероятность **пересечения** (intersection) или **произведения** (*product of events*) двух событий $A$ и $B$ характеризует вероятность того, что исход будет содержаться как в $A$, так и в $B$:

$$
P(A\cap B) \;=\; P(A)\,P(B\mid A) \;=\; P(B)\,P(A\mid B).
$$

для [[Independent and Dependent Events|независимых событий]] $P(B\mid A)=P(B)$ и $P(A\mid B)=P(A)$, поэтому

$$
P(A\cap B) = P(A)·P(B)
$$

для [[Compatible and Incompatible Events|несовместных событий]]

$$
P(A∩B)=0
$$

так как $A\cap B=\varnothing$. В результате испытания может произойти либо $A$ либо $B$.

>[!addition]- Пересечение трех и более событий
> Для пересечения событий используется **цепное правило** (*chain rule*) или **правило произведения** (*product rule*). Для трёх событий:
> $$
> P(A \cap B \cap C) = P(A) \cdot P(B|A) \cdot P(C|A \cap B)
> $$
> Логика здесь последовательная: сначала происходит $A$ с вероятностью $P(A)$, затем при условии $A$ происходит $B$ с вероятностью $P(B|A)$, и наконец, при условии что оба уже произошли, происходит $C$.
> 
> Для $n$ событий:
> $$
> P\left(\bigcap_{i=1}^n A_i\right) = P(A_1) \cdot P(A_2|A_1) \cdot P(A_3|A_1 \cap A_2) \cdots P\left(A_n \mid \bigcap_{i=1}^{n-1} A_i\right)
> $$
> Или более компактно:
> $$
> P\left(\bigcap_{i=1}^n A_i\right) = \prod_{i=1}^n P\left(A_i \mid \bigcap_{j=1}^{i-1} A_j\right)
> $$
> где при $i=1$ условие пустое, то есть $P(A_1∣\varnothing) = P(A_1)$.

>[!addition]- Пересечение взаимно независимых событий
> $$
> P\left(\bigcap_{i=1}^n A_i\right) = \prod_{i=1}^n P(A_i)
> $$

[[Joint Probability|❐]] Совместная вероятность случайных величин

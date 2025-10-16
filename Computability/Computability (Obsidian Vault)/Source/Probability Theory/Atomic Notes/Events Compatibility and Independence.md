
[[Independent and Dependent Events|Независимые]] события являются [[Compatible and Incompatible Events|совместными]], если $P(A)>0$ и $P(B)>0$, так как в этом случае этом $P(A \cap B)>0$, следовательно, $A \cap B≠\varnothing$ (условие совместности). 

Обратное неверно: совместные события могут быть как независимыми так и зависимыми. 

[[Compatible and Incompatible Events|Несовместные]] события являются [[Independent and Dependent Events|зависимыми]], если $P(A)>0$ и $P(B)>0$, так как в этом случае $A∩B=\varnothing$, следовательно, $P(A \cap B)>0$, что соответствует условию зависимости $P(A \cap B) \neq P(A) \cdot P(B)$. 

Обратное неверно: несовместные события могут быть как зависимыми, так и независимыми.

>[!explain]- Intuition
>![[Events Compatibility and Independence Intuition|no-t]]

События $A$ и $B$ одновременно несовместны и независимы в том и только в том случае, если $P(A)>0$ и $P(B)>0$.

>[!example]-
> Пусть испытанием является бросание игральной кости, пространством исходов – $\Omega = \{ 1, 2, 3, 4, 5, 6 \}$. 
> 
> События $A = \{1,2,3\}$ и $B = \{1,4\}$ являются совместными и независимыми:
> $$
> A\cap B = \{1\},\quad
> P(A\cap B) = \frac{1}{6}.
> $$
> $$
> P(A) = \frac{3}{6} = \tfrac12,\qquad
> P(B) = \frac{2}{6} = \tfrac13,
> $$
> $$
> P(A)\,P(B) = \tfrac12 \cdot \tfrac13 = \tfrac{1}{6} = P(A\cap B).
> $$
> ---
> События $A=\{ 2, 4, 6 \}$ и $B=\{ 4, 5, 6 \}$ являются совместными и зависимыми:
> $$
> A∩B = \{ 4, 6 \}, \quad P(A∩B)=\frac{1}{3} 
> $$
> $$
> P(A)=P(B)=\frac{1}{2}, \quad  P(A)·P(B) = \frac{1}{4} 
> $$
> $$
> P(A \cap B) \neq P(A) \cdot P(B)
> $$
> ---
> События $A=\{ 1, 2 \}$ и $B=\{ 5, 6 \}$ являются несовместными и зависимыми:
> $$
> A \cap B = \varnothing \quad ⇒ \quad  P(A \cap B) = 0
> $$
> $$
> P(A) = \frac{2}{6} = \frac{1}{3}, \quad P(B) = \frac{2}{6} = \frac{1}{3}
> $$
> $$
> P(A) P(B) = \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{9} \neq 0 = P(A \cap B)
> $$
> ---
> События $A=\varnothing$ и $B=\{ 1, 2, 3 \}$ являются независимыми и несовместными
> $$
> A \cap B = \varnothing \quad ⇒ \quad  P(A \cap B) = 0
> $$
> $$
> P(A) = 0, \quad P(B) = \frac{3}{6} = \frac{1}{2}
> $$
> $$
> P(A) P(B) = 0 = P(A \cap B)
> $$

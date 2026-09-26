# Lecture 1 — Mathematical Foundations

## Sources

- **Primary source:** Saarland University — Theoretical Computer Science, Lecture 1 slide.
- **Supplementary:** 
    - Dr. Trefor Bazett - [Reflexive, Symmetric, and Transitive Relations on a Set](https://youtu.be/q0xN_N7l_Kw?si=ITRK0FOAP5LLgTOe)
    - Dr. Trefor Bazett - [You need to check EVERY spot for reflexivity, symmetry, and transitivity](https://youtu.be/TctNssYMXJE?si=_SP7xDVUQdfOkzcI)
    - Areallnamesgone - [
Injective, Surjective and bi-jective](https://youtu.be/MY4-5mXfWzo?si=IHibgy1I1lRYuEvQ)
    - Dr. Trefor Bazett - [Cantor's Diagonal Argument: The rationals and reals have different sizes?!?!?](https://youtu.be/0HF39OWyl54?si=A3WqZrZWOLdIP_OH)

---

## 1. Sets

A set is a collection of distinct objects.

### Basic notation

- $x \in A$: $x$ is an element of $A$.
- $X \subseteq A$: $X$ is a subset of $A$.
- $\emptyset$: the empty set.
- $A \cup B$: union of $A$ and $B$.
- $A \cap B$: intersection of $A$ and $B$.
- $A \setminus B$: elements in $A$ but not in $B$.
- $A \times B$: Cartesian product of $A$ and $B$.

For example, if

$$
A = \{1,2,3\}
$$

then

$$
2 \in A
$$

$$
\{2\} \notin A
$$

$$
\{2\} \subseteq A.
$$


## 2. Power Set

The power set of a set $A$ is the set of all subsets of $A$.

$$
2^A = \{X \mid X \subseteq A\}
$$

If $A$ has $n$ elements, then its power set has:

$$
|2^A| = 2^{|A|} = 2^n
$$

elements.

For example:

$$
A = \{a,b,c\}
$$

Then:

$$
2^A =
\{
\emptyset,
\{a\},
\{b\},
\{c\},
\{a,b\},
\{a,c\},
\{b,c\},
\{a,b,c\}
\}
$$

Therefore:

$$
|A|=3
$$


$$
|2^A|=8.
$$


## 3. Relations

A relation between $A$ and $B$ is a subset of their Cartesian product:

$$
R \subseteq A \times B
$$


We write:

$$
aRb
$$

when:

$$
(a,b) \in R.
$$


### Reflexive

A relation $R$ on $A$ is reflexive if:

$$
\forall a \in A,\quad (a,a)\in R
$$

Intuitively, every element must be related to itself.


### Symmetric

A relation $R$ on $A$ is symmetric if:

$$
\forall a,b\in A,\quad
(a,b)\in R \Leftrightarrow (b,a)\in R
$$

Intuitively, if $a$ is related to $b$, then $b$ must also be related to $a$.


### Transitive

A relation $R$ on $A$ is transitive if:

$$
\forall a,b,c\in A,\quad
(a,b)\in R \land (b,c)\in R
\Rightarrow (a,c)\in R
$$

Intuitively:

$$
a\rightarrow b\rightarrow c
$$

must imply:

$$
a\rightarrow c.
$$

The elements $a$, $b$, and $c$ do not have to be different.

For example:

$$
1R2 \land 2R1
$$

requires:

$$
1R1
$$

for transitivity.


### Equivalence Relation

An equivalence relation is a relation that is:

1. Reflexive
2. Symmetric
3. Transitive


## 4. Equivalence Classes

For an equivalence relation $R$, the equivalence class of an element $a$ is:

$$
[a] = \{x\in A \mid xRa\}
$$

Equivalence classes group together elements that are equivalent under the relation.

For example, if:

$$
A=\{1,2,3\}
$$

$$
R=\{(1,1),(2,2),(3,3),(1,2),(2,1)\}
$$

then:

$$
[1]=[2]=\{1,2\}
$$

and:

$$
[3]=\{3\}.
$$

The equivalence classes form a partition of $A$.


## 5. Functions

A function $f:A\rightarrow B$ is a relation such that every element of $A$ has exactly one corresponding element in $B$.

In other words:

> Every input has exactly one output.

For example:

$$
f=\{(1,a),(2,b),(3,a)\}
$$

is a function from:

$$
A=\{1,2,3\}
$$

to:

$$
B=\{a,b\}.
$$

However,

$$
\{(1,a),(1,b),(2,c)\}
$$

is not a function because **the input $1$ has two different outputs.**


### Partial Function

A partial function allows each input to have **at most one** output.

Therefore:

- exactly one output → allowed
- no output → allowed
- more than one output → not allowed

Every function is also a partial function, but not every partial function is a function.


## 6. Injective, Surjective and Bijective Functions

### Injective

A function $f:A\rightarrow B$ is injective if:

$$
\forall a,b\in A,\quad
a\neq b \Rightarrow f(a)\neq f(b)
$$

Intuitively, two different inputs cannot have the same output.

Example:

$$
1\rightarrow a,\quad
2\rightarrow b,\quad
3\rightarrow c
$$

is injective.

But:

$$
1\rightarrow a,\quad
2\rightarrow a
$$

is not injective.


### Surjective

A function $f:A\rightarrow B$ is surjective if:

$$
\forall b\in B,\quad
\exists a\in A:\ f(a)=b
$$

Intuitively, every element of $B$ must be used as an output. There cannot be an unused element in $B$.


### Bijective

A function is bijective if it is both injective and surjective.

Therefore, every element of $A$ has exactly one output and every element of $B$ has exactly one input mapping to it.


### Relationship between injective and surjective functions

A function:

$$
f:A\rightarrow B
$$

is surjective if and only if there exists an injective function:

$$
g:B\rightarrow A.
$$

Because if g is injective, all of the B elements has an output different then each other. When we reverse, we know that there is no unused element in B.  
This shows the connection between the two concepts when the direction of the mapping is reversed.


## 7. Cardinality

The cardinality of a set represents its size.

For a finite set:

$$
A=\{1,2,3\}
$$

we have:

$$
|A|=3.
$$


### Comparing Cardinalities

$$
|A|\leq |B|
$$

if and only if there exists an injective function:

$$
f:A\rightarrow B.
$$

Similarly:

$$
|A|\geq |B|
$$

if and only if there exists a surjective function:

$$
f:A\rightarrow B.
$$

Two sets have the same cardinality if and only if there exists a bijection between them:

$$
|A|=|B|
\iff
\exists\text{ bijection }f:A\rightarrow B.
$$


### Example

Let:

$$
|A|=3,\qquad |B|=5.
$$

Then:

$$
|A|<|B|.
$$

An injective function from $A$ to $B$ can exist, but a surjective function from $A$ to $B$ cannot exist because $A$ has only three elements while $B$ has five.


## 8. Cantor's Theorem

For every set $A$:

$$
|A| < |2^A|.
$$

### Idea of the Proof

Assume, for contradiction, that:

$$
|2^A|\leq |A|.
$$

From the definition of cardinality, this would imply that there exists a surjective function:

$$
h:A\rightarrow 2^A.
$$

Since $h$ is assumed to be surjective, every subset of $A$ should appear as $h(a)$ for some $a\in A$.

Now construct the subset:

$$
\Delta_h=\{a\in A\mid a\notin h(a)\}.
$$

This set contains exactly those elements $a$ that are not contained in their corresponding set $h(a)$.

For every $a\in A$, the sets $h(a)$ and $\Delta_h$ differ at element $a$:

- If $a\in h(a)$, then $a\notin\Delta_h$.
- If $a\notin h(a)$, then $a\in\Delta_h$.

Therefore:

$$
\Delta_h\neq h(a)
$$

for every $a\in A$.

But:

$$
\Delta_h\in 2^A
$$

so $\Delta_h$ is a subset of $A$ that is not produced by $h$.

Therefore, $h$ cannot be surjective.

This contradicts the assumption that:

$$
|2^A|\leq |A|.
$$

Hence:

$$
\boxed{|A|<|2^A|}
$$


## Key Takeaways
- $2^A$ is the set of all subsets of $A$.
- $|A|$ is the cardinality of $A$.
- A function assigns exactly one output to every input.
- A partial function assigns at most one output to every input.
- Injective means different inputs have different outputs.
- Surjective means every element of the co-domain is reached.
- Bijective means both injective and surjective.
- Cardinality can be compared using injections, surjections and bijections.
- Cantor's theorem shows that:

$$
|A|<|2^A|
$$

for every set $A$.
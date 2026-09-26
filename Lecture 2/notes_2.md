# Lecture 2 — Countability, Strings, Languages and Computing Mechanisms

## Sources

- **Primary source:** Saarland University — Theoretical Computer Science, Lecture 2 slide.
- **Supplementary:** 
    - Mathoma - [Set Theory (Part 19): Infinite Binary Sequences and Cantor's Diagonal Argument](https://youtu.be/uWGGpPNA7Dk?si=fO-laGJ3eJMBZ83O)

---

## 1. Functions and Cardinality

### Recap: Functions

For a function $f:A\to B$:

$$
f\text{ is injective}
\iff
\forall a,a'\in A,\quad a\neq a'\Rightarrow f(a)\neq f(a')
$$

$$
f\text{ is surjective}
\iff
\forall b\in B,\ \exists a\in A:\ f(a)=b
$$

$$
f\text{ is bijective}
\iff
f\text{ is injective and surjective}
$$

---



### Equinumerous Sets

Sets $A$ and $B$ are **equinumerous** (have the same cardinality) if there exists a bijection

$$
f:A\to B.
$$

The notation means that there is a bijection between the sets; it does **not** mean that the sets are equal.

---

### Finite and Countable Sets

A set $A$ is **finite** if

$$
\exists k\in\mathbb N:\quad
A\leftrightarrow\{1,\ldots,k\}.
$$

A set $A$ is **countably infinite** if

$$
A\leftrightarrow\mathbb N.
$$

A set is **countable** if it is either finite or countably infinite.

---

# 2. Countability and Its Lemmas

The lecture develops several lemmas that allow us to prove that larger and more complicated sets are countable.

## Lemma 1.0

$$
A\text{ is countable}
\iff
\exists\text{ injection }A\to\mathbb N
\iff
\exists\text{ surjection }\mathbb N\to A.
$$

### Intuition

To show that $A$ is countable, we can either:

- assign every element of $A$ a unique natural number, or
- enumerate the elements of $A$ using $\mathbb N$.

So, intuitively:

> A countable set is a set whose elements can be listed using natural numbers.

---

## Lemma 1.1

If $B$ is countable and

$$
A\subseteq B,
$$

then $A$ is also countable.

### Intuition

A subset of a countable set cannot contain more elements than the countable set itself.

This lemma is useful because once a larger set is known to be countable, its subsets are **immediately countable** as well.

---

## Lemma 1.2

If 
$
A_1,\ldots,A_k
$ are finite sets, then

$
A_1\cup\cdots\cup A_k
$ and $ A_1\times\cdots\times A_k $ 

is finite.

### Intuition

A finite number of finite sets still gives us only finitely many elements or combinations.

For example, if

$$
|A|=3,\qquad |B|=4,
$$

then

$$
|A\times B|=3\cdot4=12.
$$

---

## Lemma 1.3

If $A_i$ is finite for every $i\in\mathbb N$, then

$$
\bigcup_{i\in\mathbb N}A_i
$$

is countable.

This is important because it allows us to combine **infinitely many finite sets** and still obtain a countable set.

### Application: $\Sigma^*$

If $\Sigma$ is a finite alphabet, then

$$
\Sigma^*=\bigcup_{i\in\mathbb N}\Sigma^i.
$$

Each $\Sigma^i$ is finite because it contains all strings of one fixed length $i$.

Therefore,

$$
\boxed{\Sigma^*\text{ is countable}.}
$$

---

## Lemma 1.4

If $A$ and $B$ are countable, then

$
A\cup B
$
and
$
A\times B
$

are countable.

### Grid intuition for $A\times B$

If

$$
A=\{a_0,a_1,a_2,\ldots\}
$$

and

$$
B=\{b_0,b_1,b_2,\ldots\},
$$

then $A\times B$ can be visualized as an infinite grid:

| | $b_0$ | $b_1$ | $b_2$ | $\cdots$ |
|---|---|---|---|---|
| $a_0$ | $(a_0,b_0)$ | $(a_0,b_1)$ | $(a_0,b_2)$ | $\cdots$ |
| $a_1$ | $(a_1,b_0)$ | $(a_1,b_1)$ | $(a_1,b_2)$ | $\cdots$ |
| $a_2$ | $(a_2,b_0)$ | $(a_2,b_1)$ | $(a_2,b_2)$ | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |


If $A , B = \mathbb{Z}$ ,the elements of $\mathbb{Z}\times\mathbb{Z}$ can be visualized as an infinite grid:

| $\mathbb{Z}\times\mathbb{Z}$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $\cdots$ |
|---|---:|---:|---:|---:|---:|---:|
| **$-2$** | $(-2,-2)$ | $(-2,-1)$ | $(-2,0)$ | $(-2,1)$ | $(-2,2)$ | $\cdots$ |
| **$-1$** | $(-1,-2)$ | $(-1,-1)$ | $(-1,0)$ | $(-1,1)$ | $(-1,2)$ | $\cdots$ |
| **$0$** | $(0,-2)$ | $(0,-1)$ | $(0,0)$ | $(0,1)$ | $(0,2)$ | $\cdots$ |
| **$1$** | $(1,-2)$ | $(1,-1)$ | $(1,0)$ | $(1,1)$ | $(1,2)$ | $\cdots$ |
| **$2$** | $(2,-2)$ | $(2,-1)$ | $(2,0)$ | $(2,1)$ | $(2,2)$ | $\cdots$ |
| **$\vdots$** | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |

The pairs can be enumerated systematically by traversing the grid.



### Application: Rational Numbers

The lecture gives the corollary:

$$
\boxed{\mathbb Q\text{ is countable}.}
$$

---



## Lemma 1.5

If $A_i$ is countable for every $i\in\mathbb N$, then

$$
\bigcup_{i\in\mathbb N}A_i
$$

is countable.

This generalizes Lemma 1.3:

- **Lemma 1.3:** every $A_i$ is finite.
- **Lemma 1.5:** every $A_i$ is countable.

### Logical Structure

The lemmas can be viewed as a chain of tools:

$$
\text{finite sets}
\rightarrow
\text{finite unions/products}
\rightarrow
\text{countable unions}
\rightarrow
\Sigma^*\text{ is countable}
$$

and

$$
A,B\text{ countable}
\rightarrow
A\times B\text{ countable}
\rightarrow
\mathbb Q\text{ countable}.
$$

The important point is that **the lemmas allow countability results to be built step by step**.

---

# 3. Cantor Diagonalization

## $2^{\mathbb N}$ and Infinite Bit Sequences

Every subset of $\mathbb N$ can be represented by a function

$$
\mathbb N\to\{0,1\}.
$$

For each $i\in\mathbb N$:

- use $1$ if $i$ belongs to the subset,
- use $0$ otherwise.

Therefore,

$$
2^{\mathbb N}
=
\mathcal P(\mathbb N)
$$

corresponds to the set of all infinite binary sequences

$$
\{\alpha\mid\alpha:\mathbb N\to\{0,1\}\}.
$$

---

## Cantor's Diagonalization

Suppose that all infinite binary sequences could be listed:

$$
\alpha_0,\alpha_1,\alpha_2,\ldots
$$

We can visualize the list as rows:

| | $0$ | $1$ | $2$ | $3$ | $4$ | $\cdots$ |
|---|---:|---:|---:|---:|---:|---|
| $\alpha_0$ | 0 | 1 | 1 | 0 | 1 | $\cdots$ |
| $\alpha_1$ | 1 | 0 | 1 | 1 | 0 | $\cdots$ |
| $\alpha_2$ | 0 | 0 | 0 | 1 | 0 | $\cdots$ |
| $\alpha_3$ | 1 | 0 | 0 | 0 | 0 | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |

Now look at the diagonal:

$$
\alpha_0(0),\alpha_1(1),\alpha_2(2),\ldots
$$

Construct a new sequence $\delta$ by changing every diagonal bit:

$$
\boxed{\delta(i)=1-\alpha_i(i)}
$$

Therefore,

$$
\delta(i)\neq\alpha_i(i)
$$

for every $i$.

So:

- $\delta\neq\alpha_0$ because they differ at position $0$.
- $\delta\neq\alpha_1$ because they differ at position $1$.
- $\delta\neq\alpha_2$ because they differ at position $2$.
- and so on.

Thus $\delta$ differs from **every** sequence on the proposed list.

Therefore, the list cannot have contained every infinite binary sequence.

Hence:

$$
\boxed{2^{\mathbb N}\text{ is not countable}.}
$$

### Core Intuition

The important idea behind diagonalization is:

> Assume that you have a complete list. Then construct an object that is guaranteed to be different from every object on that list.

The new sequence does not need to differ from each row everywhere. It only needs **one guaranteed differing position for each row**.

---

## Uncountability of the Real Numbers

The lecture then gives the corollary:

$$
\boxed{\mathbb R\text{ is not countable}.}
$$

The reason is that the real numbers between $0$ and $1$ can be represented using infinite binary sequences. Since those sequences are not countable, the real numbers cannot be countable either.

Therefore:

$$
\mathbb Q\text{ is countable}
$$

while

$$
\mathbb R\text{ is not countable}.
$$

---

# 4. Words, Strings and Languages

## Alphabet

An alphabet is a finite set of symbols, denoted by

$$
\Sigma.
$$

For example:

$$
\Sigma=\{0,1\}.
$$

---

## $\Sigma^k$

$\Sigma^k$ is the set of all strings of **exactly length $k$** over $\Sigma$.

For example, if

$$
\Sigma=\{0,1\},
$$

then

$$
\Sigma^2=\{00,01,10,11\}.
$$

Therefore,

$$
|\Sigma^2|=4.
$$

In general, if $|\Sigma|=m$, then

$$
|\Sigma^k|=m^k.
$$

---

## Empty Word

The symbol

$$
\varepsilon
$$

denotes the empty word.

Its length is

$$
|\varepsilon|=0.
$$

Therefore,

$$
\Sigma^0=\{\varepsilon\}.
$$

**The empty word belongs to $\Sigma^0$, not to every $\Sigma^k$.**

---

## $\Sigma^*$

$$
\Sigma^*=\bigcup_{k\in\mathbb N}\Sigma^k
$$

is the set of **all finite strings** over $\Sigma$.

For example, if

$$
\Sigma=\{0,1\},
$$

then

$$
10110\in\Sigma^*.
$$

---

## $\Sigma^+$

$$
\Sigma^+=\bigcup_{k>0}\Sigma^k
$$

is the set of all **non-empty finite strings** over $\Sigma$.

Therefore,

$$
\Sigma^*=\{\varepsilon\}\cup\Sigma^+.
$$

---

## Concatenation

If
$
a=a_1\ldots a_m
$
and
$
b=b_1\ldots b_n,
$
then their concatenation is

$$
a\cdot b=a_1\ldots a_mb_1\ldots b_n.
$$

For example:

$$
a=011,\qquad b=1010
$$

gives

$$
ab=0111010
$$

and

$$
ba=1010011.
$$

In general,

$$
ab\neq ba.
$$

Therefore, concatenation is not commutative.

However, there are special cases where $ab=ba$. For example:

$$
a=0,\qquad b=00
$$

gives

$$
ab=000=ba.
$$

---

## $\#_a(w)$

For 
$
w\in\Sigma^*
$
and
$
a\in\Sigma,
$
the notation

$$
\#_a(w)
$$

means the number of occurrences of symbol $a$ in $w$.

For example, for

$$
w=abbababa,
$$

we have

$
\#_a(w)=4
$
and
$
\#_b(w)=4.
$

---

## Languages

A language over an alphabet $\Sigma$ is a set of strings:

$$
\boxed{L\subseteq\Sigma^*.}
$$

For example, let

$$
\Sigma=\{a,b\}
$$

and define

$$
L=
\{w\in\Sigma^*\mid\#_a(w)=\#_b(w)\}.
$$

This language contains exactly the strings with the same number of $a$'s and $b$'s.

Thus, a language can be viewed as the collection of inputs for which the computing mechanism answers "yes".

Examples:

- $aabb\in L$
- $ababa\notin L$
- $bbaa\in L$
- $\varepsilon\in L$, because $0=0$
- $aaab\notin L$

The example with $\varepsilon$ is useful because it shows that language membership is determined by the mathematical rule, not by whether the string has a human-language meaning.

---

# 5. Computing Scenario

## Simple Computing Mechanism

A simple computing scenario can be viewed as:

$$
\text{input string}
\longrightarrow
\text{computing mechanism}
\longrightarrow
0\text{ or }1.
$$

The mechanism is recognizing a language.

Conceptually:

$$
w\longrightarrow
\begin{cases}
1 & \text{if }w\in L,\\
0 & \text{if }w\notin L.
\end{cases}
$$

---

## Abstract Computing Mechanism

The previous model treats the computing mechanism as a **black box**. The lecture now opens this black box and describes how a computation takes place step by step.

An abstract computing mechanism contains:

1. **Input tape**
2. **Control with finitely many states**
3. **Memory**
4. **Readhead**
5. **Rules for computation steps**

---

## Components

### Input Tape

The input string is placed on the input tape.

### Readhead

The readhead determines which symbol is currently being examined.

### Control with Finitely Many States

The control has a finite set of states. The current state represents the current condition of the control.

### Memory

The mechanism may have additional stored information. The exact form and accessibility of this memory depends on the particular computing model.

### Computation Rules

The rules determine what the mechanism should do at each computation step.

---

## Computation Step

A computation step depends on:

- the symbol under the readhead,
- the current state,
- the memory content.

The applicable rule then determines actions such as:

- going into a new state,
- moving the readhead,
- changing the memory content.

Conceptually:

$$
\text{current configuration}
\longrightarrow
\text{applicable rule}
\longrightarrow
\text{next configuration}.
$$

This is the transition from viewing computation as a black box to viewing it as a sequence of individual steps.

---

## Three Kinds of Computing Mechanisms

The lecture introduces three types of computing mechanisms according to how their memory works.

## 1. Finite Automaton

**No memory.**

Its computational mechanism consists of a finite set of states and transition rules.

---

## 2. Turing Machine

Memory is a tape with cells and a **read/write head**.

The head can read from and write to the tape.

---

## 3. Pushdown Automaton

Memory is a tape with cells and a **read/write head that operates only at one end of the tape**.

This gives the memory a stack-like structure.

---

## Main Idea

The central question introduced by these models is:

> **How does the available memory, and the way that memory can be accessed, affect which languages a computing mechanism can recognize?**

This becomes important in the following lectures, where finite automata and the languages they can recognize are studied formally.

---

# Key Takeaways

- A set is **countable** if it is finite or can be put into a one-to-one correspondence with $\mathbb N$.
- Lemma 1.0 gives equivalent ways of characterizing countability.
- Lemma 1.1 lets us conclude that subsets of countable sets are countable.
- Lemmas 1.2 and 1.3 build countability results from finite sets.
- Lemmas 1.4 and 1.5 extend these results to countable sets and countable unions.
- For a finite alphabet $\Sigma$, the set $\Sigma^*$ of all finite strings is countable.
- $\mathbb Q$ is countable, while $\mathbb R$ is not.
- Cantor's diagonalization constructs an object that differs from every object in a proposed complete list.
- $2^A$ denotes the power set $\mathcal P(A)$ in this context.
- $2^{\mathbb N}$ corresponds to the set of all infinite binary sequences.
- $\Sigma^k$ contains strings of exactly length $k$.
- $\Sigma^*$ contains all finite strings, including $\varepsilon$.
- $\Sigma^+$ contains all non-empty finite strings.
- A language is a subset $L\subseteq\Sigma^*$.
- A computing mechanism can be viewed as deciding whether an input string belongs to a language.
- An abstract computing mechanism consists of an input tape, finite-state control, memory, readhead, and computation rules.
- A computation proceeds through individual steps determined by the current symbol, state, memory, and applicable rules.
- **Finite does not mean small:** a finite automaton may have any finite number of states.
- What matters is whether the information that must be remembered has finitely many relevant possibilities.
- Finite automata, pushdown automata, and Turing machines differ in their memory capabilities and how that memory can be accessed.

---

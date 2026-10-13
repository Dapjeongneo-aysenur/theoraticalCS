# Lecture 3: Finite Automata and Continuation Languages

## Sources

- **Primary source:** Saarland University — Theoretical Computer Science, Lecture 2 slide.
- **Supplementary:**

---

## 1. Finite Automata

A finite automaton is a mathematical model that reads an input word one symbol at a time and changes state according to its transitions.

The lecture defines a finite automaton as

$$
M=(Q,S,s,F,D),
$$

where:

- $Q$ is a finite set of states(like $q_1$,$q_2$,...).
- $S$ is the input alphabet.(like S = {a,b,c})
- $s\in Q$ is the start state.(like $q_0$)
- $F\subseteq Q$ is the set of accepting states.(like $q_5$)
- $D\subseteq ((Q\times S)\times Q)$ is the transition relation.

A triple $(q,a,q')\in D$ means that the automaton can move from state $q$ to state $q'$ while reading symbol $a$.

### DFA and NFA

An automaton is deterministic if, for every state-symbol pair $(q,a)\in Q\times S$, there is at most one state $q'$ such that $(q,a,q')\in D$. Such an automaton is a **DFA**. Otherwise, it is an **NFA**.

The definition uses **at most one**, so a state-symbol pair may have no outgoing transition. If a computation has no transition for the next input symbol, that computation cannot consume the rest of the word.

### Configurations

The set of configurations is

$$
K_M=Q\times S^*.
$$

A configuration $(q,w)$ records the current state $q$ and the unread part of the input $w$.

For an input $x\in S^*$, the start configuration is

$$
\operatorname{start}_x=(s,x).
$$

The set of end configurations is

$$
\mathrm{Fin}=\{(f,\varepsilon)\mid f\in F\}.
$$

Thus, an end configuration must have an accepting state and no unread input. Reaching an accepting state before consuming the whole word is not enough.

## 2. Computation Steps

The one-step computation relation is defined by

$$
(q,au)\vdash_M(q',u)\quad\text{iff}\quad(q,a,q')\in D.
$$

If the machine is in state $q$ and the unread input begins with $a$, it can follow an $a$-labelled transition to $q'$. The symbol $a$ is consumed, leaving $u$ unread.

The relation $\vdash_M^*$ is the **reflexive and transitive closure** of $\vdash_M$. It describes zero or more steps:

- $\vdash_M$: one step.
- $\vdash_M^*$: zero, one, or many steps.

Zero steps are allowed. Therefore,

$$
(q,\varepsilon)\vdash_M^*(q,\varepsilon).
$$

(This fact alone does not mean that $\varepsilon$ is accepted. The state must also be accepting.)

For example, suppose the transitions include $q_0\xrightarrow{a}q_0$ and $q_0\xrightarrow{b}q_1$. On input $aab$, the computation is

$$
\begin{aligned}
(q_0,aab)&\vdash_M(q_0,ab)\\
&\vdash_M(q_0,b)\\
&\vdash_M(q_1,\varepsilon).
\end{aligned}
$$

If $q_1\in F$, this computation accepts the word!

## 3. Accepted Words and Languages

The automaton $M$ accepts input $x\in S^*$ if

$$
\operatorname{start}_x\vdash_M^*(f,\varepsilon)
\quad\text{for some }f\in F.
$$

The language accepted by $M$ is

$$
L(M)=\{x\in S^*\mid M\text{ accepts }x\}.
$$

A language $L$ is a **DFA-language** if $L=L(M)$ for some DFA $M$. It is an **NFA-language** if $L=L(M)$ for some NFA $M$.

For an NFA, one accepting computation is sufficient. Other possible computations may fail or end in non-accepting states. A word is accepted only if a computation consumes the entire input and finishes in an accepting state.

## 4. Transition Graphs

The transition graph of an automaton is $G_M=(Q,E)$. Its vertices are the states, and its labelled directed edges represent transitions:

$$
q\xrightarrow{a}q'\in E
\quad\text{iff}\quad(q,a,q')\in D.
$$


A word is accepted exactly when its symbols label a directed path from the start vertex to an accepting vertex, in order, and the path consumes the whole word. Vertices and edges may be repeated.

### Example 1: A nondeterministic automaton

The first example contains a choice of transitions on the same input symbol. The word `aabb` belongs to $L(M)$: one path is

$$
q_0\xrightarrow{a}q_1\xrightarrow{a}q_2
\xrightarrow{b}q_4\xrightarrow{b}q_5.
$$

The word `aabba` does not belong to $L(M)$. The displayed path consumes `aabb` and reaches $q_5$, but the final `a` remains unread and cannot be consumed from that state. Acceptance requires a path for the **entire** input, not only a prefix.

### Example 2: Counting modulo 3

The second example recognizes

$$
L(M)=\{a^n\mid n\bmod 3=1\}.
$$

The automaton cycles through three states when it reads `a`. The start state and accepting state determine which remainder is accepted. The accepted lengths are $1,4,7,10,\ldots$; for example, `a`, `aaaa`, and `aaaaaaa` are accepted, while `aa` is not.

The machine does not need to store the exact number of `a` symbols. It only needs to track the count modulo 3, which has three possible values: 0, 1, and 2.

## 5. Continuation Languages

Let $L\subseteq S^*$ be a language and $w\in S^*$. The continuation language of $w$ with respect to $L$ is

$$
F_L(w)=\{x\in S^*\mid wx\in L\}.
$$

It is the set of all strings that can be appended to $w$ to obtain a word in $L$.

The set of continuation languages of $L$ is

$$
\mathcal F_L=\{F_L(w)\mid w\in S^*\}.
$$

These expressions describe different things:

- $F_L(w)$ is the continuation language for one prefix $w$.
- $\mathcal F_L$ is the set of all distinct continuation languages produced by all prefixes.

Different prefixes may have the same continuation language. Thus, infinitely many prefixes do not necessarily mean infinitely many continuation languages.

### Example 1: $L=S^*$

Every string over $S$ belongs to $L$, so every continuation is valid after every prefix:

$$
F_L(w)=S^*\quad\text{for every }w\in S^*.
$$

Hence,

$$
\mathcal F_L=\{S^*\}.
$$

There is only one distinct continuation language.

### Example 2: The number of `a` symbols is divisible by 3

Let $S=\{a,b\}$ and

$$
L=\{u\in S^*\mid \#a(u)\text{ is divisible by }3\},
$$

where $\#a(u)$ is the number of `a` symbols in $u$. Define

$$
L_i=\{x\in S^*\mid \#a(x)\bmod3=i\},\quad i\in\{0,1,2\}.
$$

A continuation must supply the remainder needed to make the total number of `a` symbols divisible by 3. The lecture gives these examples:

$$
\begin{aligned}
F_L(bbab)&=\{x\in S^*\mid \#a(x)\bmod3=2\}=L_2,\\
F_L(ab)&=L_2,\\
F_L(aab)&=L_1,\\
F_L(abaab)&=L_0.
\end{aligned}
$$

For example, `ab` contains one `a`, so a valid continuation must contain a number of `a` symbols congruent to 2 modulo 3. There are only three continuation languages:

$$
\mathcal F_L=\{L_0,L_1,L_2\}.
$$

### Example 3: Equal numbers of `a` and `b`

Consider

$$
L=\{a^n b^n\mid n\in\mathbb N\}.
$$

The lecture gives the following continuation languages:

$$
F_L(bbab)=\emptyset,\qquad F_L(ab)=\{\varepsilon\},
$$

$$
F_L(aab)=\{b\},\qquad F_L(aaaaabb)=\{bbb\}.
$$

- $F_L(bbab)=\emptyset$: no continuation can turn `bbab` into a word of the form $a^n b^n$.
- $F_L(ab)=\{\varepsilon\}$: `ab` is already a complete word in the language, so only the empty continuation works.
- $F_L(aab)=\{b\}$: appending one `b` completes the word.
- $F_L(aaaaabb)=\{bbb\}$: three more `b` symbols are required.

The slide also gives

$$
F_L(aaa)=\{bbb,\ abbbb,\ aabbbbb,\ldots\}.
$$

For this language, the required continuation can depend on how many `a` symbols have already appeared. The slide describes the resulting family as

$$
\mathcal F_L=\{\emptyset\}\cup\{L_i\mid i\in\mathbb N\}\cup\{S_j\mid j\in\mathbb N\},
$$

where

$$
L_i=\{b^i\},\qquad S_j=\{a^{n-j}b^n\mid n>j\}.
$$

There are infinitely many distinct continuation languages.

## 6. DFA-Languages Have Finitely Many Continuation Languages

The lecture's lemma states

$$
L\text{ is a DFA-language}\quad\Longrightarrow\quad\mathcal F_L\text{ is finite}.
$$

### Proof idea

Suppose a DFA $M=(Q,S,s,F,D)$ recognizes $L$. For each state $q\in Q$, define

$$
L_q=\{x\in S^*\mid (q,x)\vdash_M^*(f,\varepsilon)\text{ for some }f\in F\}.
$$

If reading a prefix $w$ takes the DFA from its start state to state $p$, then

$$
F_L(w)=L_p.
$$

In other words, once the DFA has read a prefix, the possible accepted continuations depend on the state it reached. The machine does not need to remember the whole prefix.

Because the DFA has finitely many states, there are only finitely many possible sets $L_q$. If a prefix cannot be consumed because a transition is missing, its continuation language is empty, which adds at most one further set. Therefore, $\mathcal F_L$ is finite.

This lemma proves one direction only. It does not, by itself, prove that every language with finitely many continuation languages is a DFA-language!

## 7. Showing That a Language Is Not a DFA-Language

The contrapositive of the lemma is

$$
\mathcal F_L\text{ is infinite}\quad\Longrightarrow\quad L\text{ is not a DFA-language}.
$$

To prove that a language is not a DFA-language, it is sufficient to find infinitely many prefixes $w(i)$ whose continuation languages are pairwise distinct:

$$
F_L(w(i))\ne F_L(w(j))\quad\text{whenever }i\ne j.
$$

### Example 1: $L=\{a^n b^n\mid n\in\mathbb N\}$

Choose

$$
w(i)=a^i b,\quad i>0.
$$

The prefix contains $i$ copies of `a` and one copy of `b`. To complete it to a word with equal numbers of `a` and `b`, the continuation must be exactly $b^{i-1}$. Thus,

$$
F_L(w(i))=\{b^{i-1}\}.
$$

For example,

$$
F_L(ab)=\{\varepsilon\},\quad F_L(aab)=\{b\},\quad F_L(aaab)=\{bb\}.
$$

These continuation languages are distinct for different values of $i$. There are infinitely many of them, so $L$ is not a DFA-language.

### Example 2: Perfect-square lengths

Consider

$$
L=\{a^{n^2}\mid n\in\mathbb N\},\qquad w(i)=a^{i^2}.
$$

The difference between consecutive squares is

$$
(i+1)^2-i^2=2i+1.
$$

Therefore,

$$
i^2+(2i+1)=(i+1)^2,
$$

so $w(i)a^{2i+1}\in L$. If $j<i$, then $i^2+(2j+1)$ lies strictly between $i^2$ and $(i+1)^2$, so it is not a square. Hence $w(i)a^{2j+1}\notin L$.

The continuation languages for these prefixes differ: a continuation that works for one prefix does not work for the others in this family. Thus, there are infinitely many distinct continuation languages, and this language is not a DFA-language.

### Example 3: Prime lengths

Consider

$$
L=\{a^n\mid n\text{ is prime}\}.
$$

The lecture uses two facts about prime numbers:

1. For every $N$, there is a prime greater than $N$. To see why, consider $N!+1$. No integer from 2 through $N$ divides it. Any prime factor of $N!+1$ must therefore be greater than $N$. Note that $N!+1$ itself is not necessarily prime.
2. For every $K$, there is a run of at least $K$ consecutive composite numbers. The numbers

   $$
   (K+1)!+2,\ (K+1)!+3,\ldots,(K+1)!+(K+1)
   $$

   are all composite, because each number $(K+1)!+j$ is divisible by $j$ for $2\le j\le K+1$.

The lecture takes

$$
W=\{a^{i!+1}\mid i\in\mathbb N\}
$$

and applies these two facts. They provide prefixes whose continuation languages have arbitrarily large shortest non-empty words. Such continuation languages cannot all be equal. Therefore, there are infinitely many distinct continuation languages, and the language of prime-length words is not a DFA-language.

## 8. Key Takeaways

- A finite automaton is defined by its states, alphabet, start state, accepting states, and transition relation.
- A configuration records the current state and unread input.
- Acceptance requires consuming the entire input and ending in an accepting state.
- An NFA accepts a word if at least one computation path accepts it.
- $F_L(w)$ is the set of continuations that complete prefix $w$ into a word in $L$.
- $\mathcal F_L$ is the set of all distinct continuation languages.
- A DFA-language has finitely many continuation languages.
- If a language has infinitely many pairwise-distinct continuation languages, it is not a DFA-language.
- The languages of the form $\{a^n b^n\}$, perfect-square lengths, and prime lengths illustrate this proof method.

# Distinguishability of the 6-pack on $\operatorname{CL(4)}$-filtration Simplicial Complexes

## Introduction
Our topic explores the distinguishability of the 6-pack in the context of the chromatic alpha complex on a $\operatorname{CL(4)}$-filtration of two-dimensional simplicial complexes.

## Goal
Define a quantity to measure how simplicial complexes are different from each other, and measure how the 6-pack can be used to distinguish them.

## Notations and Preliminaries

- $\mathbb{I}_4\coloneqq \mathbb{I}_{\mathbb{A}_4}$. It has $10$ elements. Notice that for different convention for the death coordinate, the expression of a birth-death pair may be different. We will apply the inclusive-exclusive convention, i.e., the death coordinate is exclusive.
- Let \( X \) be a $\operatorname{CL(4)}$ filtration of simplicial complexes.
- $D(M)$: the persistence diagram of a persistence module $M$ over $\mathbb{A}_4$. It is effectively a function $\mathbb{I}_4\to \mathbb{Z}_{\geq 0}$.
- Applying homology functors \( H_0 \) and \( H_1 \) to $X$, we obtain persistence modules \( M_0 \) and \( M_1 \), both of $CL(4)$.
- For the relative homology of this simplicial complex, we get persistence modules \( N_0, N_1, N_2 \) over $\mathbb{A}_4$ where $N_p\coloneqq H_p(\overline{X}, \underline{X})$ for $p=0,1,2$.
- Consider the functor \( \mathcal{T} \) that maps from the category of $\operatorname{CL(4)}$-filtration of simplicial complexes to the product category of these five representation categories: 
  $$
  \begin{aligned}
    \mathcal{T}: \operatorname{CL(4)}\text{-filt. of s.c.s} &\to 
    \mathbf{rep}(\operatorname{CL(4)})\times\mathbf{rep}(\operatorname{CL(4)})\times\mathbf{rep}(\mathbf{A}_4)\times\mathbf{rep}(\mathbf{A}_4)\times\mathbf{rep}(\mathbf{A}_4) \\
    X &\mapsto (M_0, M_1, N_0, N_1, N_2)
  \end{aligned}
  $$

## Definitions

### Type Vector / Characteristic Vector

- The type vector of a simplicial complex \( X \) is the representation type of $\mathcal{T}(X)$ expressed as a vector consists of non-negative integers recording the multiplicity of each indecomposable. It has length \( 76 + 76 + 10 + 10 + 10 = 182 \). For simplicity we will write it as $\mathcal{T}(X)$ as well.

### Packs

- **5-pack**: Operates on a persistence module of $\operatorname{CL(4)}$ and provides five persistence diagrams. Written as an array $\vec{D}^5(M)\coloneqq (D^{kernel}(M), D^{domain}(M), D^{image}(M), D^{codomain}(M), D^{cokernel}(M))$. Where $D^{\square}(M)\coloneqq D(\square(M))$, and $\square$ refers to the operation to obtain a type $\mathbb{A}_4$ persistence module from $M$. A 5-pack is a vector of length $50$.
- **6-pack**: Operates on a $\operatorname{CL(4)}$-filtration of simplicial complexes and provides six persistence diagrams. Written as an array $\vec{D}(X)\coloneqq (*\vec{D}^5(M_0), *\vec{D}^5(M_1), D(N_0), D(N_1), D(N_2))$. Where $*$ refers to the spread operator, i.e., the elements of the array are spread out. It has length $50 + 50 + 10 + 10 + 10 = 130$.


## Properties

- Let $X_1$ and $X_2$ be two $\operatorname{CL(4)}$-filtration of simplicial complexes. Then $\mathcal{T}(X_1 \sqcup X_2)=\mathcal{T}(X_1)+\mathcal{T}(X_2)$.
- For a positive integer $n$, we define $n X\coloneqq X\sqcup X\sqcup\cdots\sqcup X$ ($n$ times).
- Consider a collection $\{X_i\}_{i=1}^n$ of $\operatorname{CL(4)}$-filtration of simplicial complexes. If their type vectors are linearly dependent over $\mathbb{Q}$, i.e., there exist $\lambda_i\in\mathbb{Q}^{\times}$ such that $\sum_{i=1}^n \lambda_i\mathcal{T}(X_i)=0$, then by multiplying a common denominator and rearranging the negative terms, we can find two configurations such that $\mathcal{T}(\bigsqcup_{i\in J_1} \lambda'_i X_i)=\mathcal{T}(\bigsqcup_{i\in J_2} \lambda'_i X_i)$ for some $J_1\sqcup J_2=\{1,2,\cdots,n\}$ and $\lambda'_i, \lambda'_i\in\mathbb{Z}_{> 0}$. The other direction is also true. Thus linear operations on the type vector correspond to constructions on the filtration of simplicial complexes.
- The same holds for the 6-pack vector.

## Searching for an indistinguishable instance

The goal is to find a collection of $\operatorname{CL(4)}$-filtration of simplicial complexes $\{X_i\}_{i=1}^n$ such that their type vectors are linearly independent, but there 6-pack vectors are linearly dependent. This is equivalent to that the rank of the matrix whose rows are the 6-pack vectors of these simplicial complexes is less than $n$, given that the rank of the matrix whose rows are the type vectors is $n$.

## Implementation of computations

1. Input: a $\operatorname{CL(4)}$-filtration of simplicial complexes $X$, where the lower row is obtained via a constant deletion of simplices.
2. Two classes for computations:
    - the type vector of $X$.
    - the 6-pack vector of $X$.
3. The computed vectors shall be stored in a dataframes, with the info about the simplicial complexes and the point cloud stored.
4. Construct matrices from the dataframes and compute the rank.
5. Find a linear combination of the rows if the rank is less than the number of rows.
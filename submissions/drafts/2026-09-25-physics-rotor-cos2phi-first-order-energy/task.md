---
id: 2026-09-25-physics-rotor-cos2phi-first-order-energy
status: draft
field: Physics
domain: Quantum Mechanics
subdomain: Perturbation theory
problem_type: Symbolic expression
answer_type: Exact symbolic expression
concepts:
  - Degenerate perturbation theory
  - Planar rigid rotor
  - Off-diagonal matrix element
  - First-order energy
routing: Automated Checks Only
independently_verified: true
working_title: rotor cos2phi first-order energy
---

## Problem

A planar rigid rotor with moment of inertia $I$ has Hamiltonian $H=-\frac{\hbar^{2}}{2I}\frac{d^{2}}{d\phi^{2}}+\lambda\cos(2\phi)$, where $\lambda>0$ and $\phi\in[0,2\pi)$. The $2\pi$-periodic eigenfunctions of the kinetic term are $\psi_m(\phi)=(2\pi)^{-1/2}e^{im\phi}$ with $m\in\mathbb{Z}$. Energies are required only through first order in $\lambda$. Report the lower energy associated with the unperturbed $|m|=1$ pair as an exact expression in $\hbar$, $I$, and $\lambda$.

## Domain Explanation

This problem involves the first-order energies of a degenerate rotor level in a $\cos(2\phi)$ potential, which are part of Quantum Mechanics and Perturbation theory.
The problem also involves $2\pi$-periodic angular eigenfunctions labeled by the integer $m$, which are part of Quantum Mechanics and Angular momentum and spin.
However, $m$ only identifies the unperturbed subspace; the asked object is a first-order energy, not an angular-momentum eigenvalue.

## Step 1

Step 1
The kinetic eigenproblem on the circle gives $E_m^{(0)}=\frac{\hbar^{2}m^{2}}{2I}$. The values $m=+1$ and $m=-1$ share $E^{(0)}=\frac{\hbar^{2}}{2I}$. Matrix elements of $V=\lambda\cos(2\phi)$ on a single $e^{im\phi}$ state vanish, $\langle m|\cos(2\phi)|m\rangle=\frac{1}{2\pi}\int_{0}^{2\pi}\cos(2\phi)\,d\phi=0$, so a nondegenerate first-order formula written on $|m|=1$ alone produces a vanishing shift.

## Step 2

Step 2
The Fourier identity $\cos(2\phi)=\frac{1}{2}(e^{2i\phi}+e^{-2i\phi})$ connects $\Delta m=\pm 2$. Inside the degenerate pair, $\langle +1|\cos(2\phi)|-1\rangle=\frac{1}{2}$, and the remaining entry is the same by Hermiticity. Coupling from $|m|=1$ to $|m|=\pm 3$ belongs to a different unperturbed energy and does not enter the first-order $2\times 2$. In the ordered basis $\{|+1\rangle,|-1\rangle\}$, $V=\begin{pmatrix} 0 & \frac{\lambda}{2} \\ \frac{\lambda}{2} & 0 \end{pmatrix}$.

## Step 3

Step 3
The eigenvalues of the matrix in Step 2 are $\pm\frac{\lambda}{2}$. Adding $E^{(0)}$ from Step 1 produces $\frac{\hbar^{2}}{2I}+\frac{\lambda}{2}$ and $\frac{\hbar^{2}}{2I}-\frac{\lambda}{2}$. With $\lambda>0$ the lower value is $\frac{\hbar^{2}}{2I}-\frac{\lambda}{2}$.

Final Answer: $\boxed{\dfrac{\hbar^{2}}{2I}-\dfrac{\lambda}{2}}$

## Answer

$\dfrac{\hbar^{2}}{2I}-\dfrac{\lambda}{2}$

## Author Notes

Local only. Never paste this section into Snorkel.
Independent check:
- [x] Hid the boxed line and recomputed $\langle +1|\cos(2\phi)|-1\rangle=1/2$ from the Fourier identity
- [ ] `python scripts/qa_gate.py` PASS
- [ ] `python scripts/preflight.py` PASS
Why a frontier model should miss this:
- Nondegenerate first-order formula on $|m|=1$ gives a vanishing diagonal, so the reported energy stays $\hbar^{2}/(2I)$.

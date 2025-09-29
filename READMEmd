# Heat Equation Solver

## Governing PDE
We are solving the **2D heat equation**:

$$
\frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} \right)
$$

where:
- $T(x, y, t)$ is the temperature field
- $\alpha$ is the thermal diffusivity
- $x, y$ are spatial coordinates
- $t$ is time

---

## Discretization

We discretize the domain using a uniform grid:
- Grid spacing: $h_x = \Delta x$, $h_y = \Delta y$
- Time step: $\Delta t$
- Indices: $i$ for $x$, $j$ for $y$, $n$ for time

For uniform grid spacing ($h_x = h_y = h$), the discretized explicit scheme is:

$$
T_{i,j}^{n+1} = T_{i,j}^n + \lambda \Big( T_{i+1,j}^n + T_{i-1,j}^n + T_{i,j+1}^n + T_{i,j-1}^n - 4T_{i,j}^n \Big)
$$

where:

$$
\lambda = \frac{\alpha \, \Delta t}{h^2}
$$

---

## Stability Condition

For the explicit 2D scheme, stability requires:

$$
\lambda \leq \frac{1}{4}
$$

which gives:

$$
\Delta t \leq \frac{h^2}{4 \alpha}
$$

---

## Implementation Parameters

From the given configuration:

- $N_x = 100$, $N_y = 100$
- $\Delta x = \Delta y = 0.1 \; (h = 0.1)$
- $\alpha = 0.1$
- $\Delta t = 0.01$

### Compute $\lambda$:

$$
\lambda = \frac{0.1 \times 0.01}{0.1^2} = \frac{0.001}{0.01} = 0.1
$$

This satisfies the stability condition since $0.1 < 0.25$.

---

## Boundary and Initial Conditions

- **Initial condition**: hot spot at center $(50, 50)$ with $T = 100$
- **Boundary conditions**: Dirichlet fixed temperatures
  - North, South, East, West = $0$


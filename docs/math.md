# Math notes

## Batch gradient descent
For MSE loss \(L(w) = \frac{1}{n}\|Xw - y\|^2\), the gradient is
\(\nabla_w L = \frac{2}{n} X^\top (Xw - y)\).

## Closed-form OLS
With centered features, \(\hat{w} = (X^\top X)^{-1} X^\top y\) (or Moore–Penrose pseudoinverse).

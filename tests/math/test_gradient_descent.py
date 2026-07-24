import numpy as np
from datamind.math.gradient_descent import (
    gradient_descent,
    numerical_gradient,
    quadratic_grad,
    quadratic_loss,
)

def test_gd_converges_to_zero():
    theta0 = np.array([3.0, -2.0])
    result = gradient_descent(
        theta0,
        grad_fn=lambda t: quadratic_grad(t, a=1.0),
        loss_fn=lambda t: quadratic_loss(t, a=1.0),
        lr=0.2,
        n_iter=100,
    )
    assert np.linalg.norm(result.params) < 1e-3
    assert result.history[-1] < result.history[0]

def test_numerical_matches_analytical():
    theta = np.array([1.0, -1.0, 0.5])
    analytical = quadratic_grad(theta)
    numerical = numerical_gradient(lambda t: quadratic_loss(t), theta)
    assert np.allclose(analytical, numerical, atol=1e-5)

import numpy as np
from datamind.math.norms import l1_norm, l2_norm
def test_norms():
    v = np.array([3.0, 4.0])
    assert abs(l2_norm(v) - 5.0) < 1e-9
    assert l1_norm(v) == 7.0

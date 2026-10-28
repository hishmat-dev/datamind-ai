import pandas as pd
from datamind.preprocessing.pipeline import PreprocessPipeline

def test_impute_scale_onehot_train_only():
    train = pd.DataFrame({"a": [1.0, None, 3.0], "b": ["x", "y", "x"]})
    test = pd.DataFrame({"a": [None, 5.0], "b": ["y", "z"]})
    pipe = PreprocessPipeline().fit(train)
    tr = pipe.transform(train)
    te = pipe.transform(test)
    assert tr["a"].isna().sum() == 0
    assert abs(tr["a"].mean()) < 1e-6
    assert any(c.startswith("b__") for c in tr.columns)
    # unseen category z → all zeros for b one-hots
    assert te.filter(like="b__").sum(axis=1).iloc[1] == 0

from datamind.explain.format_importance import format_importance_table
def test_fmt():
    t = format_importance_table({'a': 0.2, 'b': 0.5})
    assert 'b' in t.splitlines()[1]

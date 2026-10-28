from datamind.data.loader import list_datasets, load_dataset

def test_four_datasets():
    names = list_datasets()
    assert set(names) >= {"housing", "diabetes", "iris", "wine"}
    for n in names:
        b = load_dataset(n)
        assert len(b.frame) > 0 and b.target in b.frame.columns
        assert b.task in {"regression", "classification"}

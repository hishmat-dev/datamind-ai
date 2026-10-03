from datamind.analytics.experiment_note_10 import note_10

def test_note_10():
    assert note_10("ok").startswith("exp10:")

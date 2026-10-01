from datamind.analytics.experiment_note_01 import note_1

def test_note_1():
    assert note_1("ok").startswith("exp1:")

from datamind.analytics.experiment_note_02 import note_2

def test_note_2():
    assert note_2("ok").startswith("exp2:")

from datamind.analytics.experiment_note_11 import note_11

def test_note_11():
    assert note_11("ok").startswith("exp11:")

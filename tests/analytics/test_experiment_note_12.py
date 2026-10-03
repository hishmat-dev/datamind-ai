from datamind.analytics.experiment_note_12 import note_12

def test_note_12():
    assert note_12("ok").startswith("exp12:")

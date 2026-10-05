from datamind.analytics.experiment_note_21 import note_21

def test_note_21():
    assert note_21("ok").startswith("exp21:")

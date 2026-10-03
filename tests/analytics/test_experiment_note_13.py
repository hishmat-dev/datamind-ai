from datamind.analytics.experiment_note_13 import note_13

def test_note_13():
    assert note_13("ok").startswith("exp13:")

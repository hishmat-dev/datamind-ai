from datamind.analytics.experiment_note_00 import note_0

def test_note_0():
    assert note_0("ok").startswith("exp0:")

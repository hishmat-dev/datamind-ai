from datamind.analytics.experiment_note_23 import note_23

def test_note_23():
    assert note_23("ok").startswith("exp23:")

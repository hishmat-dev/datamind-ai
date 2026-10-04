from datamind.analytics.experiment_note_15 import note_15

def test_note_15():
    assert note_15("ok").startswith("exp15:")

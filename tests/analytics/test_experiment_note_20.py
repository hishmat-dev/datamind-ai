from datamind.analytics.experiment_note_20 import note_20

def test_note_20():
    assert note_20("ok").startswith("exp20:")

from datamind.analytics.experiment_note_06 import note_6

def test_note_6():
    assert note_6("ok").startswith("exp6:")

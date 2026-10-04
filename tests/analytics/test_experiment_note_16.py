from datamind.analytics.experiment_note_16 import note_16

def test_note_16():
    assert note_16("ok").startswith("exp16:")

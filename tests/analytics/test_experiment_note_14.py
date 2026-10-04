from datamind.analytics.experiment_note_14 import note_14

def test_note_14():
    assert note_14("ok").startswith("exp14:")

from datamind.analytics.experiment_note_22 import note_22

def test_note_22():
    assert note_22("ok").startswith("exp22:")

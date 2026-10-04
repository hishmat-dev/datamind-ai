from datamind.analytics.experiment_note_18 import note_18

def test_note_18():
    assert note_18("ok").startswith("exp18:")

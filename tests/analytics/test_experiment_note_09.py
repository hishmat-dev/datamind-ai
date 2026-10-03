from datamind.analytics.experiment_note_09 import note_9

def test_note_9():
    assert note_9("ok").startswith("exp9:")

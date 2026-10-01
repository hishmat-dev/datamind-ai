from datamind.analytics.experiment_note_03 import note_3

def test_note_3():
    assert note_3("ok").startswith("exp3:")

from datamind.analytics.experiment_note_05 import note_5

def test_note_5():
    assert note_5("ok").startswith("exp5:")

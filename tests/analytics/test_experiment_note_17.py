from datamind.analytics.experiment_note_17 import note_17

def test_note_17():
    assert note_17("ok").startswith("exp17:")

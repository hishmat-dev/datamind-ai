from datamind.analytics.experiment_note_24 import note_24

def test_note_24():
    assert note_24("ok").startswith("exp24:")

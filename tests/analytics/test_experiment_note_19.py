from datamind.analytics.experiment_note_19 import note_19

def test_note_19():
    assert note_19("ok").startswith("exp19:")

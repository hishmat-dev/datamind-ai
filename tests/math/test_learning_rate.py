from datamind.math.learning_rate import constant, inverse_time, step_decay

def test_schedules():
    assert constant(0.1, 50) == 0.1
    assert step_decay(0.1, 100, drop_every=100, factor=0.5) == 0.05
    assert inverse_time(0.1, 100, decay=0.01) < 0.1

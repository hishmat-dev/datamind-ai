from datamind.app.dashboard import build_overview_text

def test_overview():
    assert "500" in build_overview_text(500)
    assert "0.850" in build_overview_text(100, 0.85)

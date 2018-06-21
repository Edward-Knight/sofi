import time


def test_ui_start(chrome):
    # It takes some time to load the page
    time.sleep(1)
    assert chrome.title == 'Sofi'

from main import check_ip

def test_check_ip():
    assert check_ip("192.168.11.2") is True
    assert check_ip("100.32.15.1") is False
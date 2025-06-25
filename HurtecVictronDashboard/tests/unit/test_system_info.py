from utils.system_info import get_system_info

def test_system_info_keys():
    info = get_system_info()
    assert 'platform' in info
    assert 'release' in info

from dashboard.config_manager import load_config, save_config
import os
from tempfile import TemporaryDirectory

def test_load_and_save_config(tmp_path):
    cfg = {
        'tabs': [
            {
                'url': 'https://example.com',
                'name': 'Example',
                'username': 'user',
                'password': 'pass',
            }
        ]
    }
    os.chdir(tmp_path)
    save_config(cfg)
    loaded = load_config()
    assert loaded == cfg

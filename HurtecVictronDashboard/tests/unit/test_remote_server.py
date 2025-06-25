import pytest

try:
    from remote.server import create_app
except ModuleNotFoundError:
    pytest.skip("Flask not installed", allow_module_level=True)

class FakeTabs:
    def __init__(self):
        self.items = []
    def count(self):
        return len(self.items)
    def tabText(self, i):
        return self.items[i][1]
    def addTab(self, widget, name):
        self.items.append((widget, name))
    def removeTab(self, index):
        self.items.pop(index)

class FakeMainWindow:
    def __init__(self):
        self.tabs = FakeTabs()
    def add_tab(self, url, name, username='', password=''):
        self.tabs.addTab({'url': url, 'username': username, 'password': password}, name)


def test_add_and_remove_tab():
    mw = FakeMainWindow()
    app = create_app(mw)
    client = app.test_client()

    resp = client.post('/tabs', json={'url': 'https://example.com', 'name': 'Ex'})
    assert resp.status_code == 204
    assert mw.tabs.count() == 1
    assert mw.tabs.tabText(0) == 'Ex'

    resp = client.delete('/tabs/0')
    assert resp.status_code == 204
    assert mw.tabs.count() == 0

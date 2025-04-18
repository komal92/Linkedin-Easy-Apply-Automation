import pytest

@pytest.mark.usefixtures("setup")
class Test_hit_url:
    def test_hit_url(self):
        self.driver.get('https://google.com')
        assert 'Google' in self.driver.title


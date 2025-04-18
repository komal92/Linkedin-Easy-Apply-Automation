import pytest

import config


@pytest.mark.usefixtures("setup")
class Test_hit_url:
    def test_hit_url(self):
        self.driver.get(config.LINKEDIN_URL)
        assert 'LinkedIn' in self.driver.title


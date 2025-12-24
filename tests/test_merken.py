import pytest
from pages.merken_page import MerkenPage


@pytest.mark.usefixtures("setup")
class TestMerken:

    def test_canon_brand(self):
        mp = MerkenPage(self.driver, self.wait)
        mp.canon()

import pytest
from pages.inspiratie_page import InspiratiePage


@pytest.mark.usefixtures("setup")
class TestInspiratie:

    def test_natuurfotografie(self):
        ip = InspiratiePage(self.driver, self.wait)
        ip.natuurfotografie()

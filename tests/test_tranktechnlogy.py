import pytest


from pages.verticals_locator import verticals_locator
from pages.technology_locator import technology_locator
from pages.aboutus_locator import aboutus_locator
from pages.blog_locator import blog_locator
from pages.contactus_locator import contactus_locator
from pages.portfolio_locator import portfolio_locator
from pages.get_quote_locator import get_quote_locator
from pages.country_locator import country_locator
from pages.web_development_locator import web_development_locator
from pages.social_locator import social_locator

@pytest.mark.smoke
def test_vertical(driver):
    vertical_locator = verticals_locator(driver)
    vertical_locator.trading_submenus_click()
    vertical_locator.retail_submenus_click()
    vertical_locator.healthcare_submenus_click()
    vertical_locator.fintech_submenus_click()
    vertical_locator.custom_submenus_click()

@pytest.mark.smoke
def test_technology(driver):
    technologies_locator = technology_locator(driver)
    technologies_locator.ecommerce_submenus_click()
    technologies_locator.mobile_submenus_click()
    technologies_locator.artificial_submenus_click()

@pytest.mark.smoke
def test_aboutus(driver):
     about_locator = aboutus_locator(driver)
     about_locator.about_click()

@pytest.mark.smoke
def test_blog(driver):
     blogs_locator = blog_locator(driver)
     blogs_locator.blog_options_click()

@pytest.mark.smoke
def test_contact_form(driver):
     contact_locator = contactus_locator(driver)
     contact_locator.fill_contact_form()

@pytest.mark.smoke
def test_portfolio(driver):
     port_locator = portfolio_locator(driver)
     port_locator.portfolio_click()

@pytest.mark.smoke
def test_quote(driver):
    quote_locator = get_quote_locator(driver)
    quote_locator.fill_quote_form()

@pytest.mark.smoke
def test_country(driver):
    count_locator = country_locator(driver)
    count_locator.select_country()
#
# @pytest.mark.smoke
# def test_web(driver):
#     web_locator = web_development_locator(driver)
#     web_locator.web_development_flow()

@pytest.mark.smoke
def test_web_dev(driver):
    web_locator= web_development_locator(driver)
    web_locator.web_development_section()

@pytest.mark.smoke
def test_app_dev(driver):
    app_locator= web_development_locator(driver)
    app_locator.app_development_section()

@pytest.mark.smoke
def test_graphic_dev(driver):
    graphic_locator= web_development_locator(driver)
    graphic_locator.graphic_section()

@pytest.mark.smoke
def test_ui_ux_dev(driver):
    ux_locator= web_development_locator(driver)
    ux_locator.ux_ui_section()
#

@pytest.mark.smoke
def test_social(driver):
    socials_locator= social_locator(driver)
    socials_locator.social_links()
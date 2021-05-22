from framework import wait_element_by
from page_objects.catalog_page import CatalogPage


def test_catalog(browser, opencart_base_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open(opencart_base_url, 20)
    wait_element_by(browser, catalog_page.BREADCRUMBS)
    wait_element_by(browser, catalog_page.SIDEBAR)
    wait_element_by(browser, catalog_page.LIST_VIEW_BUTTON)
    wait_element_by(browser, catalog_page.GRID_VIEW_BUTTON)
    wait_element_by(browser, catalog_page.PAGINATION_INFO)

from framework import get_element


def test_catalog(browser, opencart_base_url, catalog_page):
    catalog_page.open(opencart_base_url, 20)
    get_element(browser, catalog_page.BREADCRUMBS)
    get_element(browser, catalog_page.SIDEBAR)
    get_element(browser, catalog_page.LIST_VIEW_BUTTON)
    get_element(browser, catalog_page.GRID_VIEW_BUTTON)
    get_element(browser, catalog_page.PAGINATION_INFO)

from framework import wait_element_by_link_text, wait_element_by_css_selector, wait_element_by_xpath, \
    wait_element_by_id, wait_element_by_class_name


def test_homepage(browser, opencart_base_url):
    browser.get(opencart_base_url)
    wait_element_by_link_text(browser, 'Desktops')
    wait_element_by_css_selector(browser, '#search input')
    wait_element_by_xpath(browser, '/html/body/footer/div/p/a')
    wait_element_by_id(browser, 'search')
    wait_element_by_class_name(browser, 'dropdown-toggle')

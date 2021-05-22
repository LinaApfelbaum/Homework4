from framework import wait_element_by_link_text, wait_element_by_css_selector, wait_element_by_xpath, \
    wait_element_by_id, wait_element_by_class_name


def test_catalog(browser, opencart_base_url):
    browser.get(opencart_base_url +
                "/index.php?route=product/category&path=20")
    wait_element_by_link_text(browser, 'MP3 Players')
    wait_element_by_css_selector(browser, 'li.dropdown')
    wait_element_by_xpath(
        browser, '//*[@id="content"]/div[4]/div[5]/div/div[2]/div[1]/p[1]')
    wait_element_by_id(browser, 'menu')
    wait_element_by_class_name(browser, 'input-group-addon')

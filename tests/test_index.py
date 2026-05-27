"""
Tests for the basic content of the index.html file of a personal web site.

Requires Selenium 4.6+ (uses Selenium Manager to auto-manage chromedriver)
and a recent installation of Google Chrome.
"""

import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def _build_url(site_url, page=""):
  base = site_url.rstrip("/")
  if not page:
    return base + "/"
  return base + "/" + page.lstrip("/")


class Tests:

  @pytest.fixture(scope="class")
  def settings(self):
    with open('./settings.json', 'r') as f:
      yield json.load(f)

  @pytest.fixture(scope="class")
  def driver(self, settings):
    options = Options()
    options.add_argument("--window-size=1400,1000")
    driver = webdriver.Chrome(options=options)
    driver.get(_build_url(settings["site_url"]))
    yield driver
    driver.quit()

  def test_title(self, driver, settings):
    """The page title must include the student's name."""
    assert settings["name"] in driver.title

  def test_h1(self, driver, settings):
    """There must be an h1 containing the student's name."""
    elem = driver.find_element(By.TAG_NAME, "h1")
    assert settings["name"] in elem.text

  def test_ol_exists(self, driver):
    """There must be an ordered list with at least 2 items."""
    elems = driver.find_elements(By.CSS_SELECTOR, "ol li")
    assert len(elems) >= 2

  def test_link_to_topic_page(self, driver):
    """The home page must link to topic_of_interest.html."""
    try:
      elem = driver.find_element(
        By.CSS_SELECTOR,
        "a[href='topic_of_interest.html'], a[href$='/topic_of_interest.html']",
      )
    except NoSuchElementException:
      elem = None
    assert elem, "Missing link to 'topic_of_interest.html'."

  def test_link_text_exists(self, driver):
    """At least one link must mention the JQuery assignment."""
    elems_text = ''.join(
      x.text.strip().lower().replace('assignment', '')
      for x in driver.find_elements(By.CSS_SELECTOR, "a")
    )
    assert 'jquery' in elems_text, "No link text mentions 'JQuery'."

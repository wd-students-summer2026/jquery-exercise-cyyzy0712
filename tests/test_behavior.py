"""
Tests for the interactive jQuery behaviors on topic_of_interest.html.

Requires Selenium 4.6+ (uses Selenium Manager to auto-manage chromedriver)
and a recent installation of Google Chrome.
"""

import json
import pytest
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
  def page_url(self, settings):
    return _build_url(settings["site_url"], "topic_of_interest.html")

  @pytest.fixture(scope="class")
  def driver(self, page_url):
    options = Options()
    options.add_argument("--window-size=1400,1000")
    driver = webdriver.Chrome(options=options)
    driver.get(page_url)
    # wait until jQuery has been loaded by the page (script element ordering)
    WebDriverWait(driver, 10).until(
      lambda d: d.execute_script("return typeof window.jQuery !== 'undefined'")
    )
    yield driver
    driver.quit()

  def test_jquery_loaded(self, driver):
    """jQuery must be loaded on the page (window.jQuery defined)."""
    has_jq = driver.execute_script("return typeof window.jQuery !== 'undefined'")
    assert has_jq, (
      "window.jQuery is undefined. Make sure your <script> tag for "
      "jquery.min.js loads before main.js in the <head>."
    )

  def test_main_js_loaded(self, settings):
    """The student's main.js file must be downloadable."""
    url = _build_url(settings["site_url"], "js/main.js")
    try:
      with urlopen(url, timeout=10) as resp:
        body = resp.read().decode("utf-8", errors="ignore")
        assert resp.status == 200
        assert body.strip() != "", "js/main.js is empty."
    except Exception as e:
      raise AssertionError("Could not load {} : {}".format(url, e))

  def _trigger(self, driver, trigger, event):
    """Apply a click/mouseover/mouseout event to the trigger element."""
    if event == "click":
      try:
        trigger.click()
      except Exception:
        driver.execute_script("arguments[0].click();", trigger)
    elif event == "mouseover":
      driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", trigger
      )
      ActionChains(driver).move_to_element(trigger).pause(0.3).perform()
    elif event == "mouseout":
      driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", trigger
      )
      ActionChains(driver).move_to_element(trigger).pause(0.3).perform()
      body = driver.find_element(By.TAG_NAME, 'body')
      ActionChains(driver).move_to_element(body).pause(0.3).perform()
    else:
      raise ValueError("Unknown trigger_event: {}".format(event))

  def test_image_swap(self, driver, settings):
    """
    The image swap target must change its src on mouseover, and revert
    on mouseout.
    """
    cfg = settings["jquery_settings"]["image_swap"]
    target = driver.find_element(By.CSS_SELECTOR, cfg["trigger_element_selector"])
    driver.execute_script(
      "arguments[0].scrollIntoView({block: 'center'});", target
    )

    original_src = target.get_attribute('src')

    ActionChains(driver).move_to_element(target).pause(0.4).perform()
    mouseover_src = target.get_attribute('src')

    body = driver.find_element(By.TAG_NAME, 'body')
    ActionChains(driver).move_to_element_with_offset(body, 0, 0).pause(0.4).perform()
    mouseout_src = target.get_attribute('src')

    assert original_src != mouseover_src, (
      "Image swap target's src did not change on mouseover."
    )
    assert original_src == mouseout_src, (
      "Image swap target's src did not revert on mouseout."
    )

  def test_content_change(self, driver, settings):
    """
    The text content of the content-change target must differ after the
    trigger event fires.
    """
    cfg = settings["jquery_settings"]["content_change"]
    trigger = driver.find_element(By.CSS_SELECTOR, cfg["trigger_element_selector"])
    target = driver.find_element(By.CSS_SELECTOR, cfg["target_element_selector"])
    event = cfg["trigger_event"]

    original_text = target.text

    self._trigger(driver, trigger, event)
    ActionChains(driver).pause(0.5).perform()

    # re-resolve in case jQuery replaced the node
    target = driver.find_element(By.CSS_SELECTOR, cfg["target_element_selector"])
    new_text = target.text

    assert new_text != original_text, (
      "Content-change target text did not change after {} on trigger.".format(event)
    )

  def test_animation(self, driver, settings):
    """The animated target's CSS position must change after the trigger event."""
    cfg = settings["jquery_settings"]["animation"]
    trigger = driver.find_element(By.CSS_SELECTOR, cfg["trigger_element_selector"])
    target = driver.find_element(By.CSS_SELECTOR, cfg["target_element_selector"])
    event = cfg["trigger_event"]

    before = {
      side: target.value_of_css_property(side)
      for side in ('left', 'right', 'top', 'bottom')
    }

    self._trigger(driver, trigger, event)
    # jQuery's default animation duration is 400ms; give it a bit more
    ActionChains(driver).pause(1.5).perform()

    target = driver.find_element(By.CSS_SELECTOR, cfg["target_element_selector"])
    after = {
      side: target.value_of_css_property(side)
      for side in ('left', 'right', 'top', 'bottom')
    }

    moved = any(before[s] != after[s] for s in before)
    assert moved, (
      "Animation target did not change any of left/right/top/bottom after "
      "the trigger event. Make sure the target's CSS `position` is set to "
      "`relative` or `absolute` and that animate() targets these properties."
    )

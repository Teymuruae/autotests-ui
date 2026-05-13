from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    no_results_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    no_results_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    no_results_descr = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")

    expect(title).to_be_visible()
    expect(title).to_have_text("Courses")
    expect(no_results_text).to_be_visible()
    expect(no_results_text).to_have_text("There is no results")
    expect(no_results_icon).to_be_visible()
    expect(no_results_descr).to_be_visible()
    expect(no_results_descr).to_have_text("Results from the load test pipeline will be displayed here")

import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have
from selene.support.conditions.have import exact_text

from mobile_wiki_diploma.data.language import language
from mobile_wiki_diploma.data.search_queries import (
    appium_search_query,
    selene_search_query,
    invalid_search_query,
)


@allure.feature('Search')
@allure.title('Search results render for valid search query')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Search')
@allure.severity(Severity.CRITICAL)
def test_search_for_appium():
    # When
    with allure.step('Click on Skip button'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()

    with allure.step(f'Search for {appium_search_query.query}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            appium_search_query.query
        )

    # Then
    with allure.step(f'Search results should contain {appium_search_query.query}'):
        results = browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        )
        results.should(have.size_greater_than(0))
        results.first.should(have.text(appium_search_query.query))


@allure.feature('Search')
@allure.title('Search for invalid query doesn\'t return results')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Search')
@allure.severity(Severity.CRITICAL)
def test_search_for_invalid_query():
    # When
    with allure.step('Click on Skip button'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()

    with allure.step(f'Search for {invalid_search_query.query}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            invalid_search_query.query
        )

    # Then
    with allure.step(f'No results should show for {invalid_search_query.query}'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/results_text'))
        results.should(have.exact_text('No results'))


@allure.feature('Article')
@allure.title('Article successfully opens')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Article')
@allure.severity(Severity.CRITICAL)
def test_search_and_open_article_for_testing():
    # When
    with allure.step('Click on Skip button'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()

    with allure.step(f'Search for {selene_search_query.query}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            selene_search_query.query
        )
    with allure.step('Open the first article'):
        results = browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        )
        results.first.click()

    # Then
    with allure.step(f'Article title should be {selene_search_query.query}'):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(
            have.exact_text(selene_search_query.query)
        )


@allure.feature('Onboarding')
@allure.title('Onboarding screens have correct titles')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Onboarding')
@allure.severity(Severity.CRITICAL)
def test_onboarding_screens():
    # Given
    continue_button = browser.element(
        (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
    )
    title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))

    # When
    with allure.step('Click on Continue button'):
        continue_button.click()
    with allure.step('Verify the page title is "New ways to explore"'):
        title.should(have.exact_text('New ways to explore'))

    with allure.step('Click on Continue button'):
        continue_button.click()
    with allure.step('Verify the page title is "Reading lists with sync"'):
        title.should(have.exact_text('Reading lists with sync'))

    with allure.step('Click on Continue button'):
        continue_button.click()
    with allure.step('Verify the page title is "Send anonymous data"'):
        title.should(have.exact_text('Send anonymous data'))

    with allure.step('Click on Accept button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()

    # Then
    with allure.step('Verify the main page is opened'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')
        ).should(be.visible)


@allure.feature('Language switch')
@allure.title('Language is successfully added to the list of languages')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Language switch')
@allure.severity(Severity.CRITICAL)
def test_language_is_successfully_added():
    # When
    with allure.step('Click on Skip button'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()

    with allure.step('Click on searchbar'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step('Click on Language button'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/search_lang_button')
        ).click()

    with allure.step(f'Choose language {language.language}'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/wiki_language_title')
        ).second.click()
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/localized_language_name')
        ).element_by(exact_text(language.language)).click()

    # Then
    with allure.step(
        f'Language {language.language} should be added to the list of languages'
    ):
        results = browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/wiki_language_title')
        )
        results.should(have.size(3))
        results.second.should(have.exact_text(language.language))

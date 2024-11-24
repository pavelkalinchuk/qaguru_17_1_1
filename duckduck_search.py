from selene import browser, be, have

browser.config.timeout = 20
browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('github yashaka/selene').press_enter()
browser.element('.react-results--main').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
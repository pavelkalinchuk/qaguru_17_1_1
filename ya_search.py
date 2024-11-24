from selene import browser, be, have

browser.config.timeout = 20
browser.open('https://ya.ru')
browser.element('[id="text"]').should(be.blank).type('github yashaka/selene').press_enter()
browser.element('[id="search-result"]').should(have.text('User-oriented Web UI browser tests in Python'))
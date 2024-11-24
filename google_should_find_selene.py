from selene import browser, be, have

browser.open('https://www.google.com/ncr')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text("yashaka/selene: User-oriented Web UI browser tests in Python"))

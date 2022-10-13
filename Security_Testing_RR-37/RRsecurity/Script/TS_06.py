def TS_06():
    Log.Message("6.  Check whether after giving valid credentials page is getting redirected to security questions page or not", "")
    KeywordTests.Admin_login.Run()
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.FindElement("#flash_error"), "contentText", cmpContains, "Logged in successfully.", False)
    Aliases.browser.pageEdit.imageLogout.Click()
    Delay(10000)
    KeywordTests.Close_Browser.Run()
    Delay(10000)

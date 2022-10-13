def TS_12():
    my_password = "......"
    Log.Message("12.  Verify that important i.e. sensitive information such as passwords should not get displayed in the input box when typing. They should be encrypted and in asterix / dot format.", "")
    TestedApps.chrome.Run()
    Browsers.Item[btChrome].Navigate(Project.Variables.URL)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.Click()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.SetText("manju1")
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(my_password)
    Delay(10000)
    KeywordTests.Close_Browser.Run()

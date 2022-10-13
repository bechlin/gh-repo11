﻿def TS_17():
    Log.Message("17. Verify that restricted page should not be accessible by user after session time out.", "")
    KeywordTests.Admin_login.Run()
    Delay(1205000, "Waiting for session time out")
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.panelFlashNotice, "contentText", cmpContains, "Signed out successfully.", False)
    Browsers.Item[btChrome].Navigate(Project.Variables.URL + "/dashboard")
    Delay(10000)
    Aliases.browser.BrowserWindow.Maximize()
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.FindElement("//li[contains(text(), 'Please login to continue')]"), "contentText", cmpContains, "Please login to continue", False)
    KeywordTests.Close_Browser.Run()

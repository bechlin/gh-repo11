﻿def TS_01():
    Log.Message("1.  Try to directly access bookmarked web page without login to the system.", "")
    KeywordTests.Admin_login.Run()
    Aliases.chrome.BrowserWindow.Maximize()
    NameMapping.Sys.chrome.pageEdit3.FindChildByXPath ("//div[@id='link_bar']/a[2]/img" , True).Click()
    Delay(1000)
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.panelFlashNotice, "contentText", cmpContains, "Signed out successfully.", False)
    Aliases.chrome.BrowserWindow.Click(280, 27)
    Aliases.chrome.ToUrl(Project.Variables.URL + "/admin/batch/new_work_list")
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.FindElement("//li[contains(text(), 'Please login to continue')]"), "contentText", cmpContains, "Please login to continue", False)
    Aliases.browser.pageLogin.textnodePleaseLoginToContinue.textnodePleaseLoginToContinue
    KeywordTests.Close_Browser.Run()
    Delay(1000)



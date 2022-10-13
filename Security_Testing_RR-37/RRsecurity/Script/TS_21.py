def TS_21():
    KeywordTests.Open_Revremit_login_page.Run()
    Browsers.Item[btChrome].Navigate(Project.Variables.URL)
    Aliases.browser.BrowserWindow.Maximize()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_21"].CellByName["A3"].Value
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.SetText(LastResult)
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.Keys("[Tab]")
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_21"].CellByName["B3"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult1)
    Aliases.browser.pageRevRemit2.formNewUser.submitbuttonLogin.ClickButton()
    Delay(10000)
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.FindElement("#flash_notice"), "contentText", cmpContains, "Invalid user/password combination.", False)
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.panelPageContainer, "contentText", cmpContains, "Restricted Access\nPlease login to continue\nLogin\nUser Name:\nPassword:\nForgot password", False)
    KeywordTests.Close_Browser.Run()
    Delay(5000)

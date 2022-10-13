def TS_13():
    Log.Message("13.  Verify whether your server lock out an individual who has tried to access your site multiple times with invalid login/password information?", "")
    TestedApps.chrome.Run()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B4"].Value
    Browsers.Item[btChrome].Navigate(LastResult)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_13"].CellByName["A3"].Value
    Aliases.browser.pageEdit.formNewUser.textboxUserid.SetText(LastResult1)
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_13"].CellByName["B3"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult2)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_13"].CellByName["C3"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult3)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Delay(10000)
    Aliases.browser.pageRevRemit.Wait()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_13"].CellByName["D3"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult4)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Delay(10000)
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.panelFlashError, "contentText", cmpContains, "Your account is locked. Please contact the RevRemit Administrators or Supervisors", False)
    KeywordTests.Close_Browser.Run()
    Delay(10000)

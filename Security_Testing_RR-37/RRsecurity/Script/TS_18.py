def TS_18():
    Log.Message("18.  Password authentication, the same account on different machines cannot log on at the same time. ", "")
    KeywordTests.Admin_login.Run()
    Browsers.Item[btEdge].Navigate(Project.Variables.URL + "/users/login")
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageRevRemit2.Wait()
    Aliases.browser.pageRevRemit2.Wait()
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.Click()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B8"].Value
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.SetText(LastResult)
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.Keys("[Tab]")
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C8"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult1)
    Aliases.browser.pageRevRemit2.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit2.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["D8"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult2)
    Aliases.browser.pageEdit.textboxAns1.Keys("[Tab]")
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["E8"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns2.Keys("[Tab]")
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["F8"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult4)
    Aliases.browser.pageEdit.button.ClickButton()
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.textnodeASessionIsAlreadyRunning, "contentText", cmpContains, "A session is already running using same user credentials. Please click\nhere\nto log out from previous session or contact admin.", False)
    Aliases.browser.pageEdit.linkHere.Click()
    Aliases.browser.BrowserWindow.Close()
    Delay(1000)
    Aliases.chrome.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.imageLogout.Click()
    Delay(10000)
    KeywordTests.Close_Browser.Run()
    Delay(5000)

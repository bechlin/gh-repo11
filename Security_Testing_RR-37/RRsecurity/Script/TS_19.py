﻿def TS_19():
    TestedApps.chrome.Run()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B4"].Value
    Browsers.Item[btChrome].Navigate(LastResult)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_19"].CellByName["A3"].Value
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
    Delay(1000)
    Aliases.browser.pageRevRemit.Wait()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_13"].CellByName["D3"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult4)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Delay(1000)
    KeywordTests.Close_Browser.Run()
    Delay(10000)

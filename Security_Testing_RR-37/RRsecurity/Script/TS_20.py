﻿def TS_20():
    Log.Message("20.  Add or modify important information (passwords), check if it gets reflected immediately or caching the old values.", "")
    TestedApps.chrome.Run()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B4"].Value
    Browsers.Item[btChrome].Navigate(LastResult)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B8"].Value
    Aliases.browser.pageEdit.formNewUser.textboxUserid.SetText(LastResult1)
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C8"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult2)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Delay(10000)
    Aliases.browser.pageRevRemit.Wait()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["E3"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["F3"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult4)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult5 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["G3"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult5)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textnodeUserAdministration.linkUserAdministration.Click()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageUser.textboxToFind.Click()
    LastResult6 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["B3"].Value
    Aliases.browser.pageUser.textboxToFind.SetText(LastResult6)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.imageEdit.Click()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult7 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["D3"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult7)
    Aliases.browser.pageEdit.passwordboxConfirmPassword2.Click()
    LastResult8 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["D3"].Value
    Aliases.browser.pageEdit.passwordboxConfirmPassword2.SetText(LastResult8)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.imageLogout.Click()
    Delay(10000)
    Aliases.browser.pageRevRemit.Wait()
    LastResult9 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["B3"].Value
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.SetText(LastResult9)
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.Click()
    LastResult10 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_20"].CellByName["C3"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult10)
    Aliases.browser.pageRevRemit2.formNewUser.submitbuttonLogin.ClickButton()
    Delay(5000)
    KeywordTests.Close_Browser.Run()
    Delay(10000)

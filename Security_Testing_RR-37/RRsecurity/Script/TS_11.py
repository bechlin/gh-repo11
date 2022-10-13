def TS_11():
    Log.Message("11. Check whether user is able to change password only once with in a time period using the link sent via mail", "")
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["B4"].Value
    Browsers.Item[btChrome].Run(LastResult)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["C4"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult1)
    Aliases.browser.pageEdit.formNewUser.passwordboxConfirmNewPassword.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["D4"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxConfirmNewPassword.SetText(LastResult2)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.wndChrome_WidgetWin_1.Close()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["E4"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["F4"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult4)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult5 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["G4"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult5)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.imageLogout.Click()
    LastResult6 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["B4"].Value
    Browsers.Item[btChrome].Run(LastResult6)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult7 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["C4"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult7)
    Aliases.browser.pageEdit.formNewUser.passwordboxConfirmNewPassword.Click()
    LastResult8 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["D4"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxConfirmNewPassword.SetText(LastResult8)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()

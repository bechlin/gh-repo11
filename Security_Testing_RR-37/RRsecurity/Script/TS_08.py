﻿def TS_08():
    Log.Message("8. Check whether the account is getting locked after giving wrong aswers for the security questions consecutively 3 times", "")
    TestedApps.chrome.Run()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B4"].Value
    Browsers.Item[btChrome].Navigate(LastResult)
    Aliases.browser.BrowserWindow.Maximize()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["B3"].Value
    Aliases.browser.pageEdit.formNewUser.textboxUserid.SetText(LastResult1)
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["B4"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult2)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Delay(10000)
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["A6"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["B6"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult4)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult5 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["C6"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult5)
    Aliases.browser.pageEdit.button.ClickButton()
    Delay(10000)
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult6 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["A7"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult6)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult7 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["B7"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult7)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult8 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["C7"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult8)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult9 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["A8"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult9)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult10 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["B8"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult10)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult11 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_08"].CellByName["C8"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult11)
    Aliases.browser.pageEdit.button.ClickButton()
    Delay(10000)
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.panelFlashError, "contentText", cmpContains, "Your account is locked. Please contact the RevRemit Administrators or Supervisors.", False)
    Aliases.browser.BrowserWindow.Close()
    Delay(10000)

﻿def TS_10():
    TestedApps.chrome.Run()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B4"].Value
    Browsers.Item[btChrome].Navigate(LastResult)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.formNewUser.linkForgotPassword.Click()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.formNewUser.emailinputUserEmail.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["B2"].Value
    Aliases.browser.pageEdit.formNewUser.emailinputUserEmail.SetText(LastResult1)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["E4"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult2)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["F4"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_10"].CellByName["G4"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult4)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.OUTLOOK.wndrctrl_renwnd32.rctrl_renwnd32.AfxWndW.AfxWndW.page32770.AfxWndA.panelDocument1.panelMessage.MouseWheel(0)

﻿def TS_05():
    Log.Message("5.  As part of MFA, Check whether the user is able to login only after giving  valid credentials and right aswers to security questions", "")
    KeywordTests.Admin_login.Run()
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit2.Wait()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B8"].Value
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.SetText(LastResult)
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.Keys("[Tab]")
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C10"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult1)
    Aliases.browser.pageRevRemit2.formNewUser.submitbuttonLogin.ClickButton()
    Delay(5000)
    aqObject.CheckProperty(Aliases.browser.pageRevRemit2.panelFlashNotice, "contentText", cmpContains, "Invalid user/password combination.", False)
    Aliases.browser.BrowserWindow.Close()
    Delay(10000)

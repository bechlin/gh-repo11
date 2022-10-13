﻿def TS_04():
    Log.Message("4. Check the valid and invalid passwords, check whether system comply with password rules and policies. ", "")
    KeywordTests.Admin_login.Run()
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.chrome.BrowserWindow.Maximize()
    Aliases.chrome.pageEdit3.textnodeUserAdministration.linkUserAdministration.Click()
    Aliases.browser.pageUser.linkNewUser.Click()
    Aliases.browser.pageNew.Wait()
    Aliases.browser.pageNew.textboxName.Click()
    Project.Variables.TS_04.Reset()
    RecordIdx = 1
    while RecordIdx < 6:
        Project.Variables.TS_04.Next()
        RecordIdx = RecordIdx + 1
    RecordIdx = 6
    while RecordIdx <= 11:
        Delay(500)
        LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_04"].CellByName["A3"].Value
        TimeoutValue = Options.Run.Timeout
        Options.Run.Timeout = 10000
        Aliases.browser.pageNew.textboxName.SetText(LastResult)
        Options.Run.Timeout = TimeoutValue
        Aliases.browser.pageNew.textboxUserLogin.Click()
        LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_04"].CellByName["B3"].Value
        Aliases.browser.pageNew.textboxUserLogin.SetText(LastResult1)
        Aliases.browser.pageNew.passwordboxPassword.Click()
        Aliases.browser.pageNew.passwordboxPassword.SetText(Project.Variables.TS_04.Value["F1"])
        Aliases.browser.pageNew.passwordboxConfirmPassword.Click()
        Aliases.browser.pageNew.passwordboxConfirmPassword.SetText(Project.Variables.TS_04.Value["F2"])
        Aliases.browser.pageNew.checkboxOadmin.ClickChecked(True)
        Aliases.browser.pageNew.checkboxUserImagePermision.ClickChecked(True)
        Aliases.browser.pageNew.checkboxUserImage835Permision.ClickChecked(True)
        Aliases.browser.pageNew.checkboxUserImageGridPermision.ClickChecked(True)
        Aliases.browser.pageNew.checkboxUserClaimRetrievalPermis.ClickChecked(True)
        Aliases.browser.pageNew.checkboxUserWorklistPermission.ClickChecked(True)
        Aliases.browser.pageNew.checkboxUserCheckIndexPermission.ClickChecked(True)
        Aliases.browser.pageNew.textboxUserEmployeeId.Click()
        Aliases.browser.pageNew.textboxUserEmployeeId.SetText("87987897")
        Aliases.browser.pageNew.textboxUserL1Manager.Click()
        Aliases.browser.pageNew.textboxUserL1Manager.SetText("L1")
        Aliases.browser.pageNew.textboxUserL2Manager.Click()
        Aliases.browser.pageNew.textboxUserL2Manager.SetText("L2")
        Aliases.browser.pageNew.button.ClickButton()
        Options.Run.Timeout = 20000
        aqObject.CheckProperty(Aliases.browser.pageUser.panelErrorexplanation, "contentText", cmpContains, Project.Variables.TS_04.Value["F3"], False)
        Project.Variables.TS_04.Next()
        Options.Run.Timeout = TimeoutValue
        RecordIdx = RecordIdx + 1
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_04"].CellByName["A3"].Value
    Options.Run.Timeout = 20000
    Aliases.browser.pageNew.textboxName.SetText(LastResult2)
    Options.Run.Timeout = TimeoutValue
    Aliases.browser.pageNew.textboxUserLogin.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_04"].CellByName["B3"].Value
    Aliases.browser.pageNew.textboxUserLogin.SetText(LastResult3)
    Aliases.browser.pageNew.passwordboxPassword.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_04"].CellByName["A12"].Value
    Aliases.browser.pageNew.passwordboxPassword.SetText(LastResult4)
    Aliases.browser.pageNew.passwordboxConfirmPassword.Click()
    LastResult5 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_04"].CellByName["B12"].Value
    Aliases.browser.pageNew.passwordboxConfirmPassword.SetText(LastResult5)
    Aliases.browser.pageNew.checkboxOadmin.ClickChecked(True)
    Aliases.browser.pageNew.checkboxUserImagePermision.ClickChecked(True)
    Aliases.browser.pageNew.checkboxUserImage835Permision.ClickChecked(True)
    Aliases.browser.pageNew.checkboxUserImageGridPermision.ClickChecked(True)
    Aliases.browser.pageNew.checkboxUserClaimRetrievalPermis.ClickChecked(True)
    Aliases.browser.pageNew.checkboxUserWorklistPermission.ClickChecked(True)
    Aliases.browser.pageNew.checkboxUserCheckIndexPermission.ClickChecked(True)
    Aliases.browser.pageNew.textboxUserEmployeeId.Click()
    Aliases.browser.pageNew.textboxUserEmployeeId.SetText("87987897")
    Aliases.browser.pageNew.textboxUserL1Manager.SetText("L1")
    Aliases.browser.pageNew.textboxUserL2Manager.Click()
    Aliases.browser.pageNew.textboxUserL2Manager.SetText("L2")
    Aliases.browser.pageNew.button.ClickButton()
    aqObject.CheckProperty(Aliases.browser.pageUser.panelFlashNotice, "contentText", cmpContains, "User was successfully created.", False)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.chrome.BrowserWindow.Maximize()
    Aliases.chrome.pageEdit3.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    Delay(800)
    Aliases.chrome.BrowserWindow.Close()
    Delay(900)

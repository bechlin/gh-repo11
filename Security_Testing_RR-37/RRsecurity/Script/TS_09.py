def TS_09():
    Log.Message("9. Check whether the user is able to reset the password and  security questions once the admin unlocks the account", "")
    KeywordTests.Admin_login.Run()
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.textnodeUserAdministration.linkUserAdministration.Click()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageUser.textboxToFind.Click()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["A5"].Value
    Aliases.browser.pageUser.textboxToFind.Keys(LastResult)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.imageEdit.Click()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["B5"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.Keys(LastResult1)
    Aliases.browser.pageEdit.passwordboxConfirmPassword2.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["B5"].Value
    Aliases.browser.pageEdit.passwordboxConfirmPassword2.Keys(LastResult2)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.FindElement("#flash_notice"), "contentText", cmpContains, "User was successfully updated.", False)
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["A5"].Value
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.SetText(LastResult3)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["B5"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult4)
    Aliases.browser.pageRevRemit2.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.Click()
    LastResult5 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["C5"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult5)
    Aliases.browser.pageEdit.passwordboxConfirmPassword.Click()
    LastResult6 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["C5"].Value
    Aliases.browser.pageEdit.passwordboxConfirmPassword.SetText(LastResult6)
    Aliases.browser.pageEdit.button.ClickButton()
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.panelFlashError, "contentText", cmpContains, "Signed out successfully.", False)
    Aliases.browser.BrowserWindow.Maximize()
    LastResult7 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["A5"].Value
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.SetText(LastResult7)
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.Keys("[Tab]")
    LastResult8 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["C5"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult8)
    Aliases.browser.pageRevRemit2.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.selectUserSecretQuestionsQn1.ClickItem("What was your high school’s mascot?")
    Aliases.browser.pageEdit.selectUserSecretQuestionsQn2.ClickItem("What was the name of your first pet?")
    Aliases.browser.pageEdit.selectUserSecretQuestionsQn3.ClickItem("In what town or city did you attend high school?")
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult9 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["G5"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult9)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult10 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["H5"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult10)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult11 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["TS_09"].CellByName["I5"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult11)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.imageLogout.Click()
    Delay(10000)
    Aliases.browser.BrowserWindow.Close()

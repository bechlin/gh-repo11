def TS_33():
    TestedApps.chrome.Run()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B4"].Value
    Browsers.Item[btChrome].Navigate(LastResult)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B9"].Value
    Aliases.browser.pageEdit.formNewUser.textboxUserid.SetText(LastResult1)
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C9"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult2)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["D9"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["E9"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult4)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult5 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["F9"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult5)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Project.Variables.batch_id = DBTables.TS_33.Values[0,1]  
    Project.Variables.check_number = DBTables.TS_33.Values[0,2] 
    Project.Variables.job_id = DBTables.TS_33.Values[0,0]
    Aliases.browser.ToUrl(Project.Variables.URL + "/insurance_payment_eobs/claimqa?batch_id=" + Project.Variables.batch_id  + "&checknumber=" + Project.Variables.check_number + "&first_qa=1&job_id=" + Project.Variables.job_id )
    Aliases.browser.pageRevRemit.Wait()
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.textnodeYouHaveAccessedAnInvalid, "contentText", cmpContains, "You have accessed an invalid page!", False)
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    KeywordTests.Close_Browser.Run()
    Delay(5000)

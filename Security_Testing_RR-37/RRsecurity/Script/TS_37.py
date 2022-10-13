﻿def TS_37():
    Log.Message("37. Verify whether the completed C&S jobs are not able to acess by other users by editing the url values")
    TestedApps.chrome.Run()
    Browsers.Item[btChrome].Navigate(Project.Variables.URL)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.Click()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B10"].Value
    Aliases.browser.pageEdit.formNewUser.textboxUserid.SetText(LastResult)
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C10"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult1)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["D10"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult2)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["E10"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["F10"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult4)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.chrome.BrowserWindow.Maximize()
    Aliases.chrome.pageEdit3.textnodeClientDocumentation.linkMyDataLiftTasks.Click()
    Aliases.chrome.pageNew.Wait()
    Project.Variables.batch_id = DBTables.TS_37_1.Values[0,1]  
    Project.Variables.job_id = DBTables.TS_37_1.Values[0,0] 
    Aliases.browser.ToUrl(Project.Variables.URL + "/insurance_payment_eobs/claim?allow_special_characters=true&batch_id=" + Project.Variables.batch_id +  "/&checknumber=123121&first=1&job_id=" + Project.Variables.job_id + "/&mode=NON_VERIFICATION")
    aqObject.CheckProperty(Aliases.chrome.pageNew.FindElement("#page_container"), "contentText", cmpContains, "You are not authorized to view this page", False)
    Aliases.browser.pageRevRemit.Wait()
    Delay(1000)
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.formNewUser.textboxUserid.Click()
    LastResult5 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B9"].Value
    Aliases.browser.pageEdit.formNewUser.textboxUserid.SetText(LastResult5)
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.Click()
    LastResult6 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C9"].Value
    Aliases.browser.pageEdit.formNewUser.passwordboxUserPassword.SetText(LastResult6)
    Aliases.browser.pageEdit.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.browser.pageEdit.textboxAns1.Click()
    LastResult7 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["D9"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult7)
    Aliases.browser.pageEdit.textboxAns2.Click()
    LastResult8 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["E9"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult8)
    Aliases.browser.pageEdit.textboxAns3.Click()
    LastResult9 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["F10"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult9)
    Aliases.browser.pageEdit.button.ClickButton()
    Aliases.browser.pageRevRemit.Wait()
    Aliases.chrome.BrowserWindow.Maximize()
    Aliases.chrome.pageEdit3.textnodeClientDocumentation.linkMyTasks.Click()
    Project.Variables.batch_id = DBTables.TS_37_2.Values[0,1]  
    Project.Variables.check_number = DBTables.TS_37_2.Values[0,2] 
    Project.Variables.job_id = DBTables.TS_37_2.Values[0,0] 
    Aliases.browser.ToUrl(Project.Variables.URL + "/insurance_payment_eobs/claimqa?batch_id=" + Project.Variables.batch_id + "&checknumber=" + Project.Variables.check_number + "&first_qa=1&job_id=" + Project.Variables.job_id )
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.FindElement("#flash_notice"), "contentText", cmpContains, "The batch is in OUTPUT_GENERATED status. Please contact the admin to change the status, and try again.", False)
    Aliases.chrome.BrowserWindow.Maximize()
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    KeywordTests.Close_Browser.Run()


﻿def TS_31():
    Log.Message("31. Verify that new jobs are not accessible to any processor/QA/ClipStich/Provider users by editing the url values ", "")
    KeywordTests.Open_Revremit_login_page.Run()
    Aliases.browser.BrowserWindow.Maximize()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B10"].Value
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.SetText(LastResult)
    Aliases.browser.pageRevRemit2.formNewUser.textboxUserid.Keys("[Tab]")
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C10"].Value
    Aliases.browser.pageRevRemit2.formNewUser.passwordboxUserPassword.SetText(LastResult1)
    Aliases.browser.pageRevRemit2.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.browser.pageRevRemit2.Wait()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["D10"].Value
    Aliases.browser.pageEdit.textboxAns1.SetText(LastResult2)
    Aliases.browser.pageEdit.textboxAns1.Keys("[Tab]")
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["E10"].Value
    Aliases.browser.pageEdit.textboxAns2.SetText(LastResult3)
    Aliases.browser.pageEdit.textboxAns2.Keys("[Tab]")
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["F10"].Value
    Aliases.browser.pageEdit.textboxAns3.SetText(LastResult4)
    Aliases.browser.pageEdit.textboxAns3.Keys("[Tab]")
    Aliases.browser.pageEdit.button.ClickButton()
    Browsers.Item[btChrome].Navigate(Project.Variables.URL + "/processor/my_job?location=dashboard")
    Project.Variables.batch_id = DBTables.TS_31_1.Values[0,0]  
    Project.Variables.check_number = DBTables.TS_31_1.Values[0,1] 
    Project.Variables.job_id = DBTables.TS_31_1.Values[0,2] 
    Aliases.chrome.ToUrl(Project.Variables.URL + "/insurance_payment_eobs/claim?allow_special_characters=true&batch_id=" + Project.Variables.batch_id + "&checknumber=" + Project.Variables.check_number + "&first=1&job_id=" + Project.Variables.job_id + "&mode=NON_VERIFICATION" )
    Aliases.browser.BrowserWindow.Maximize()
    aqObject.CheckProperty(Aliases.browser.pageRevRemit.textnodeYouHaveAccessedAnInvalid, "contentText", cmpContains, "401 - Unauthorized", False)
    Aliases.browser.pageEdit.imageLogout.Click()
    Delay(100)
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageRevRemit2.Wait()
    KeywordTests.Close_Browser.Run()
    Delay(10000)

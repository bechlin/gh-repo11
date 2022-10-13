def TS_22():
    Log.Message("22.  Verify the images of one client won’t be viewed by other clients.", "")
    KeywordTests.Open_Revremit_login_page.Run()
    Aliases.chrome.BrowserWindow.Maximize()
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B12"].Value
    Aliases.chrome.pageNew2.formNewUser.textboxUserid.SetText(LastResult)
    Aliases.chrome.pageNew2.formNewUser.textboxUserid.Keys("[Tab]")
    LastResult1 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C12"].Value
    Aliases.chrome.pageNew2.formNewUser.passwordboxUserPassword.SetText(LastResult1)
    Aliases.chrome.pageNew2.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.chrome.pageNew2.Wait()
    Aliases.chrome.pageEdit3.textboxAns1.Click()
    LastResult2 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["D12"].Value
    Aliases.chrome.pageEdit3.textboxAns1.SetText(LastResult2)
    Aliases.chrome.pageEdit3.textboxAns2.Click()
    LastResult3 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["E12"].Value
    Aliases.chrome.pageEdit3.textboxAns2.SetText(LastResult3)
    Aliases.chrome.pageEdit3.textboxAns3.Click()
    LastResult4 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["F12"].Value
    Aliases.chrome.pageEdit3.textboxAns3.SetText(LastResult4)
    Aliases.chrome.pageEdit3.button.ClickButton()
    Aliases.chrome.pageNew2.Wait()
    Aliases.browser.pageRevRemit.textnodeUploadBatch.linkUploadBatch.Click()
    Aliases.chrome.pageEdit3.Wait()
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxBatchid.Click()
    Data1 = DBTables.TS_22_1.Values[0,0]
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxBatchid.SetText(Data1)
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateFrom.Click()
    Date3 = DBTables.TS_22_1.Values[0,1]
    Date4 = DateTimeToFormatStr(Date3, "%Y-%m-%d")
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateFrom.SetText(Date4)
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateTo.Click()
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateTo.SetText(Date4)
    Aliases.chrome.pageNew2.formEOptions.fieldsetUndefined.selectClient.ClickItem("CHILDRENS HOSPITAL OF ORANGE COUNTY")
    Aliases.chrome.pageNew2.formEOptions.buttonFilter.ClickButton()
    Aliases.chrome.pageEdit3.Wait()
    aqObject.CheckProperty(Aliases.chrome.pageEdit3.panelNoRecordsFound, "contentText", cmpContains, "No records found", False)
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    KeywordTests.Close_Browser.Run()
    Delay(5000)
    
    
    KeywordTests.Open_Revremit_login_page.Run()
    Aliases.chrome.BrowserWindow.Maximize()
    Aliases.chrome.pageNew2.Wait()
    LastResult6 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B12"].Value
    Aliases.chrome.pageNew2.formNewUser.textboxUserid.SetText(LastResult6)
    Aliases.chrome.pageNew2.formNewUser.textboxUserid.Keys("[Tab]")
    LastResult7 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["C12"].Value
    Aliases.chrome.pageNew2.formNewUser.passwordboxUserPassword.SetText(LastResult7)
    Aliases.chrome.pageNew2.formNewUser.submitbuttonLogin.ClickButton()
    Aliases.chrome.pageNew2.Wait()
    Aliases.chrome.pageEdit3.textboxAns1.Click()
    LastResult8 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["D12"].Value
    Aliases.chrome.pageEdit3.textboxAns1.SetText(LastResult8)
    Aliases.chrome.pageEdit3.textboxAns2.Click()
    LastResult9 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["E12"].Value
    Aliases.chrome.pageEdit3.textboxAns2.SetText(LastResult9)
    Aliases.chrome.pageEdit3.textboxAns3.Click()
    LastResult10 = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["F12"].Value
    Aliases.chrome.pageEdit3.textboxAns3.SetText(LastResult10)
    Aliases.chrome.pageEdit3.button.ClickButton()
    Aliases.chrome.pageNew2.Wait()
    Aliases.browser.pageRevRemit.textnodeUploadBatch.linkUploadBatch.Click()
    Aliases.chrome.pageEdit3.Wait()
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxBatchid.Click()
    LastResult57 = DBTables.TS_22_2.Values[0,0]
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxBatchid.SetText(LastResult57)
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateFrom.Click()
    Date5 = DBTables.TS_22_2.Values[0,1]
    Date6 = DateTimeToFormatStr(Date5, "%Y-%m-%d")
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateFrom.SetText(Date6)
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateTo.Click()
    Aliases.chrome.pageEdit3.formEOptions.fieldsetUndefined.textboxDateTo.SetText(Date6)
    Aliases.chrome.pageNew2.formEOptions.fieldsetUndefined.selectClient.ClickItem("CHILDRENS HOSPITAL OF ORANGE COUNTY")
    Aliases.chrome.pageNew2.formEOptions.buttonFilter.ClickButton()
    Aliases.chrome.pageEdit3.Wait()
    aqObject.CheckProperty(Aliases.chrome.pageEdit3.panelNoRecordsFound, "contentText", cmpContains, "Displaying records", False)
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    KeywordTests.Close_Browser.Run()
    Delay(5000)
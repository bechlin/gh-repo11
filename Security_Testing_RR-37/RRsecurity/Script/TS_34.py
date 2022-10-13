def TS_34():
    Log.Message("34. Verify that the client and facility users are not able to access MPI search datas of other clients and facilities by editing url values", "")
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
    Aliases.browser.pageEdit.Wait()
    Aliases.browser.pageEdit.textnodeClientDocumentation.linkMyDataLiftTasks.Click()
    Aliases.browser.pageRevRemit2.Wait()
    Aliases.browser.pageEdit.linkDataCaptureId1.Click()
    Aliases.browser.BrowserWindow.Maximize()
    Delay(10000)
    Aliases.browser.pageEdit.Wait()
    Project.Variables.patient_account_number = DBTables.TS_34_1.Values[0,0]
    Aliases.browser.pageEdit.frameMyiframe.formForm1.textboxPatientAccountId.SetText(Project.Variables.patient_account_number)
    Aliases.browser.pageEdit.frameMyiframe.formForm1.buttonMpi.Click()
    Delay(4000)
    Project.Variables.patient_account_number = DBTables.TS_34_2.Values[0,0]
    Browsers.Item[btChrome].Navigate("https://revremit-qa.internal.guidehouse.com/immediate/mpi_searches?mpi_apply=true&page_no=1&patient_no=" + Project.Variables.patient_account_number + "&role=processor&claimleveleob=false&job_id=899586&mode=new&proc_start_time=2022-10-10+05%3A42%3A05+-0400&facility_id=2069&client_id=23&grid_type=Insurance&mpi_search_type=FACILITY&exact_serach=1&statement_id=0&cp_id=0&bb_id=0")
    Aliases.browser.wndChrome_WidgetWin_12.Close()
    Aliases.browser.pageEdit.imageMyHomeLinkImage.Click()
    Aliases.browser.pageEdit.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    KeywordTests.Close_Browser.Run()
    Delay(10000)

def TS_02():
    Log.Message("2.  Verify that system should restrict you to download the file without sign in on the system.", "")
    KeywordTests.Admin_login.Run()
    Aliases.browser.pageRevRemit.textnodeUploadBatch.linkDownloadOutput.Click()
    Aliases.browser.pageIndex.imageLogout.Click()
    Aliases.browser.pageRevRemit.Wait()
    Delay(100)
    Regions.panelFlashNotice.Check(Aliases.browser.pageRevRemit2.panelFlashNotice)
    Aliases.browser.BrowserWindow.Click(278, 29)
    LastResult = Excel.Open("C:\\Security_Testing_RR-37\\Resources\\Security_Testing_Input.xls").SheetByTitle["Sec_Input"].CellByName["B4"].Value
    Aliases.browser.ToUrl(LastResult)
    KeywordTests.Close_Browser.Run()
    Delay(1000)

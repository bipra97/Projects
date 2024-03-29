﻿# First we create the request.
$HTTP_Request = [System.Net.WebRequest]::Create('https://www.hackerrank.com')

# We then get a response from the site.
$HTTP_Response = $HTTP_Request.GetResponse()

# We then get the HTTP code as an integer.
$HTTP_Status = [int]$HTTP_Response.StatusCode

If ($HTTP_Status -eq 200) {
    Write-Host "Site is OK!"
    $python="C:\Users\91858\Anaconda3\python.exe"
    $MyPythonScript="C:\Users\91858\Desktop\alert.py"

    & $python $MyPythonScript
}
Else {
    Write-Host "The Site may be down, please check!"
}

# Finally, we clean up the http request by closing it.
If ($HTTP_Response -eq $null) { } 
Else { $HTTP_Response.Close() }
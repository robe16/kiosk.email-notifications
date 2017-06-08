# kiosk.grandparent-message-board

A mini project to create a 'kiosk' for a relative to display key information during the day.

The terminal will be a Raspberry Pi powered screen with Chromium browser auto-open in kiosk mode. Python code will also auto-run and listen on localhost:8080 for the Chromium browser to connect to.

I aim for the information and messages to be 'dementia friendly' (research to be undertaken regarding this).

Developed so far:
- Current 'time' (e.g. "Now it's Thursday monrning")
- Current/next carer information (when and name). This is taken from the weekly schedule hosted by [AxisCare](https://1000.axiscare.com)
- Messages input onto Google Sheet presented on GUI
- Day 'progress' bar presented at bottom of GUI including 'now bar', carer blocks and sunrise/set markers.

Yet to investigate and develop:
- Weather (today/tomorrow/this afternoon/etc. ??)
- Messages (and maybe images) emailed to dedicated mailbox from a safelist of senders (e.g. family members)

<kbd>
  <img src="https://github.com/robe16/kiosk.grandparent-message-board/blob/master/screenshots/screenshot_01.png">
</kbd>

<hr>

<h3>Google API</h3>

The Python 'server' utilises Google APIs to retrieve information from Google Sheets and Gmail.

In order to retrieve credentials for accessing the Google APIs (Access and Refresh Tokens), manually run the <code>/src/google/google_setup.py</code> module. This will open a browser window for logging in and authorising the application to access the user data. Once authorisation is granted, the Python application will recieve back the required credentials and these will be saved in the <code>/src/google/credentials</code> directory.

OAuth authorisation is is also requested for Google Calendar for future development purposes. 

<h4>Google Sheets: Messages</h4>

A Google Sheet is required to be setup in order to input and retrieve messages. Users can share this Google Sheet with others (e.g. family members) so that collaborators can add and amend messages when required.

The advantage of Google Sheets for this is the ability to access the file via most devices that have internet connectivity thanks to the Sheets app being available on multiple platforms.

The following format should be adopted (note: conditional formatting is not essential and does not impact Python scripts). All data should be in ranges <code>A2:D</code> as row 1 is reserved for headers.

<kbd>
  <img src="https://github.com/robe16/kiosk.grandparent-message-board/blob/master/screenshots/googlesheet_messages_01.png">
</kbd>

Within the <code>/src/config/cfg.py</code> module, change the variable <code>google_sheetId</code> to reflect the Google Sheet ID for the file created above. This can be extracted from the URL whilst accessing the file via a web browser.

In order to utilise the 'countdown' functionality, use <code>{countdown}</code> within the body of the messages (column A) and input a valid date into the 'Countdown date' cell (column B). The Python script will check if a countdown target date is present for the message, and if so, uses the <code>.format()</code> function to input the number of days to the countdown target date.

<hr>

<h3>Required python packages</h3>
<p>The following python packages require installation on the target system:
<br>
bottle: <code>http://bottlepy.org/docs/dev/index.html</code>
<br>
requests: <code>http://docs.python-requests.org/en/master/</code>
<br>
Google API client: <code>https://pypi.python.org/pypi/google-api-python-client</code>
</p>

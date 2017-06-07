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

<h3>Required python packages</h3>
<p>The following python packages require installation on the target system:
<br>
bottle: <code>http://bottlepy.org/docs/dev/index.html</code>
<br>
requests: <code>http://docs.python-requests.org/en/master/</code>
<br>
Google API client: <code>https://pypi.python.org/pypi/google-api-python-client</code>
</p>

import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from log.log import log_general


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at /credentials/sheets.googleapis.com-python-messageboard.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly https://mail.google.com/ https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'google_client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(os.path.dirname(__file__), 'credentials')
    # credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'sheets.googleapis.com-python-messageboard.json')
    # credential_path = os.path.join(credential_dir, 'sheets.googleapis.com-python-messageboard.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        log_general('Storing credentials to ' + credential_path)
    return credentials
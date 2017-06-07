# Instructions followed: https://developers.google.com/sheets/api/quickstart/python

from __future__ import print_function

import httplib2
from apiclient import discovery

from src.google.google_credentials import get_credentials


def get_data(google_sheetId, google_sheetRange):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    #
    result = service.spreadsheets().values().get(spreadsheetId=google_sheetId, range=google_sheetRange).execute()
    return result.get('values', [])



# Instructions followed: https://developers.google.com/sheets/api/quickstart/python

from __future__ import print_function
import base64
import email
import httplib2
from apiclient import discovery

from src.google.google_credentials import get_credentials


def get_api_service():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    return discovery.build('gmail', 'v1', http=http)


def get_gmail_lists(user_id='me', label_ids=[]):
    service = get_api_service()
    #
    try:
        response = service.users().messages().list(userId=user_id,
                                                   labelIds=label_ids).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id,
                                                       labelIds=label_ids,
                                                       pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages
    except Exception as e:
        return False


def get_gmail_message(msg_id, user_id='me'):
    service = get_api_service()
    #
    try:
        return service.users().messages().get(userId=user_id, id=msg_id).execute()
    except Exception as e:
        return False


def get_gmail_message_mime(msg_id, user_id='me'):
    service = get_api_service()
    #
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()
        #
        msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
        #
        mime_msg = email.message_from_string(msg_str)

        return mime_msg
    except Exception as e:
        return False

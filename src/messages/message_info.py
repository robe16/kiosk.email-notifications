from datetime import datetime

from src.messages.google_sheet import get_data
from src.messages.message import messageDetails
from src.log.console_messages import print_error, print_msg


def messages_current():
    msgObjs = get_messages()
    msgs = []
    for m in msgObjs:
        msgs.append(m.msg())
    return {'messages': msgs}


def get_messages(all=False):
    # Default will only retrieve current messages
    #
    values = get_data()
    #
    msgs = []
    #
    if not values:
        print_error('Problem encountered when processing messages from Google Sheet - No data found')
    else:
        for row in values:
            try:
                msg = row[0]
                start = datetime.strptime(row[2], '%d/%m/%Y')
                end = datetime.strptime(row[3], '%d/%m/%Y')
                #
                if not row[1] == '':
                    countdown_target = datetime.strptime(row[1], '%d/%m/%Y')
                    msgObj = messageDetails(msg, start, end, countdown_target=countdown_target)
                else:
                    msgObj = messageDetails(msg, start, end)
                #
                if all or msgObj.is_current():
                    msgs.append(msgObj)
                #
            except Exception as e:
                print_error('Problem encountered when processing message from Google Sheet - {error}'.format(error=e))
        return msgs

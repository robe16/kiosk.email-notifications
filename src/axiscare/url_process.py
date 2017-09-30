from multiprocessing import Process
from bs4 import BeautifulSoup
import time

from google.google_gmail import get_gmail_lists, get_gmail_message_mime, delete_gmail_message
from config.cfg import put_config_axiscare_url
from log.console_messages import print_msg, print_error


def eml_list():
    return get_gmail_lists()


def get_ids(id_list):
    ids = []
    for l in id_list:
        ids.append(l['id'])
    return ids


def get_emails(ids):
    emls = []
    for id in ids:
        e = get_gmail_message_mime(id)
        emls.append({'id': id, 'email': e})
    return emls


def extract_url(eml):
    #
    for p in eml.get_payload():
        if not isinstance(p.get_payload(), str):
            for p2 in p.get_payload():
                for h in p2._headers:
                    if h[0]== 'Content-Type' and h[1].startswith('text/html'):
                        payload = p2.get_payload()
                        soup = BeautifulSoup(payload, "html.parser")
                        a_all = soup.findAll("a")
                        for a in a_all:
                            href = a.attrs['href'].replace('3D', '').replace('\"', '')
                            if href.startswith('https://1000.axiscare.com'):
                                #Assumption that html version appears before pdf version
                                return href
    #
    return False


def process_emls(emls):
    #
    for e in emls:
        #
        url = extract_url(e['email'])
        #
        if url:
            put_config_axiscare_url(url)
            #Delete email
            delete_gmail_message(e['id'])
            return True
    return False


def url_updater():
    #
    updatestatus = False
    #
    while True:
        #
        try:
            eml_lists = eml_list()
            #
            if len(eml_lists) > 0:
                #
                eml_ids = get_ids(eml_lists)
                #
                if len(eml_ids) > 0:
                    #
                    emls = get_emails(eml_ids)
                    updatestatus = process_emls(emls)
            #
            if updatestatus:
                msg_success = 'the url stored in config.json has been updated'
            else:
                msg_success = 'no new urls recieved'
            print_msg('Axiscare URL updater process completed - {msg_success}'.format(msg_success=msg_success))
            #
        except Exception as e:
            print_error('Could not process emails to check for new URL notification - {error}'.format(error=e))
        #
        time.sleep(300) #5mins


def start_url_updater():
    process_urlupdater = Process(target=url_updater)
    process_urlupdater.start()
    print_msg('Axiscare URL updater process started')


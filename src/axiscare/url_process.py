from multiprocessing import Process
from bs4 import BeautifulSoup
import time

from src.google.google_gmail import get_gmail_lists, get_gmail_message_mime, delete_gmail_message
from src.axiscare.url import put_url, check_url
from src.log.console_messages import print_msg, print_error


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
    count = 0
    #
    for e in emls:
        #
        url = extract_url(e['email'])
        #
        if url:
            if not check_url(url):
                put_url(url)
                count += 1
            #Delete email either way (i.e. new or repeat url)
            delete_gmail_message(e['id'])
    #
    return count


def url_updater():
    #
    count = 0
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
                    count = process_emls(emls)
            print_msg('Axiscare URL updater process completed - {count} URL(s) updated'.format(count=count))
            #
        except Exception as e:
            print_error('Could not process emails to check for new URL notification - {error}'.format(error=e))
        #
        time.sleep(300) #5mins


def start_url_updater():
    process_urlupdater = Process(target=url_updater)
    process_urlupdater.start()
    print_msg('Axiscare URL updater process started')


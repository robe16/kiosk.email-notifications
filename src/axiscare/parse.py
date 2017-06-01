from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def getCarerNext(data):
    #
    soup = BeautifulSoup(data)
    #
    dt = datetime.now()
    carers = parseDailyCarers(soup, dt)
    carer = checkCarers(carers, dt)
    #
    if not bool(carer):
        dt = datetime.now() + timedelta(days=1)
        carers = parseDailyCarers(soup, dt)
        carer = checkCarers(carers, dt)
        #
        if not bool(carer):
            raise Exception
    #
    return carer


def parseDailyCarers(soup, d):
    #
    carers = []
    #
    class_date = "calendar-day-{date}".format(date=d.strftime("%Y-%m-%d"))
    #
    dayitem = soup.findAll("td", {"class": class_date})[0]
    daydetails = dayitem.findAll("td", {"class": "calendar_event_cell"})[0]
    careritems = daydetails.findAll("table", {"class": "cal_item cal_item_visit visit_assigned"})
    #
    for i in careritems:
        cTime = i.findAll("span", {"class": "cal_time"})[0].string
        cTime = cTime[:-((cTime.index(')'))-(cTime.index(' (')-2))]
        #
        cStart = datetime.combine(d.date(), datetime.strptime(cTime[:5], '%H:%M').time())
        cEnd = datetime.combine(d.date(), datetime.strptime(cTime[6:], '%H:%M').time())
        #
        cName = i.findAll("tr", {"class": "person caregiver assigned"})[0].contents[0].string
        #
        c = {"name": cName,
             "start": cStart,
             "end": cEnd}
        #
        carers.append(c)
        #
    return carers


def checkCarers(carers, dt):
    #
    for c in carers:
        if c['start']>dt:
            return {'when': 'next',
                    'name': c['name'],
                    'start': c['start'],
                    'end': c['end']}
        elif c['start']>dt and c['end']>dt:
            return {'when': 'current',
                    'name': c['name'],
                    'start': c['start'],
                    'end': c['end']}
    #
    raise False
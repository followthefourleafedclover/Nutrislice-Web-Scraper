from datetime import datetime, timedelta, date
import requests
import json
import smtplib
from email.message import EmailMessage

class getMenu:
    def __init__(self):
        self.date = date.today()
        print("Today's Lunch")
        self.SEND_EMAIL(self.GET(self.date.isoformat()), self.date.isoformat())
        print("Tomorrow's Lunch")
        self.SEND_EMAIL(self.GET((self.date + timedelta(days=1)).isoformat()), (self.date + timedelta(days=1)).isoformat())
    
    def GET(self, _date):
        items = []
        DIR = 'https://glastonburyus.nutrislice.com/menu/api/weeks/school/glastonbury-high/menu-type/lunch/'
        FULL = DIR + _date.split('-')[0] + '/' + _date.split('-')[1] + '/' + _date.split('-')[2]
        data = requests.get(FULL)
        print(data.status_code)
        data_JSON = json.loads(data.text)
        for date in data_JSON['days']:
            if date['date'] == _date:
                day_data = date['menu_items']
                for index, food in enumerate(day_data):
                    print(day_data[index]['food']['name'])
                    items.append(day_data[index]['food']['name'])
        if len(items) is 0:
            return "Nothing"
        else:
            return items
    
    def SEND_EMAIL(self, info, date):
        user = #Configured email address 
        pw = #email OAuth password 
        recv = #email address of recepient
        if isinstance(info, str):
            body = info
        else:
            body = ', '.join(map(str, info))
        em = EmailMessage()
        em['From'] = user
        em['To'] = recv
        em['Subject'] = f'{date} Lunch'
        em.set_content(body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, pw)
        server.sendmail(user, recv, em.as_string())
        
if __name__ == '__main__':
    getMenu()

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=credentials)




from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

# 日付を指定（例: 2023年10月28日）
date = datetime(2023, 10, 28).isoformat() + 'Z'

events_result = service.events().list(calendarId='primary', timeMin=date + 'T00:00:00Z', timeMax=date + 'T23:59:59Z',
                                      singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items')

if not events:
    print('当日の予定はありません。')
else:
    print('当日の予定:')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f'{start} - {event["summary"]}')

from __future__ import print_function
import pickle
import os.path
import datetime
import pandas
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
creds = None
def Get_Yesterday_File():
    yesterday=(datetime.date.today() - datetime.timedelta(days=1)).strftime("%b-%d-%Y")
    yesterday_file=yesterday + '.xlsx'
    try:
        pandas.read_excel(yesterday_file)
        return yesterday_file
    except Exception:
        return None
def Authentication():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive']

    global creds
    creds=None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
def Send_Data_To_Drive(file):
    global creds
    Authentication()

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': file}
    media = MediaFileUpload(file,
                            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def append_row(data, BASE_PATH):
    json_file = os.path.join(BASE_PATH, 'client_secret.json')
    print("CLient Secret ", json_file)
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_file)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1eYejJ1ywhqlTF1KIGGmTTAzpwD6TuyvBPSqdsfHHCsA").sheet1
    sheet.append_row(data)
    return True
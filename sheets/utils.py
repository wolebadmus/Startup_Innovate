import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def append_row(data, BASE_PATH):
    creds = ServiceAccountCredentials.from_json_keyfile_name("/home/webapp/client_secret.json")
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1eYejJ1ywhqlTF1KIGGmTTAzpwD6TuyvBPSqdsfHHCsA").sheet1
    sheet.append_row(data)
    return True
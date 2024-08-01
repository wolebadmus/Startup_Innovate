import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load credentials from the key file
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json')

# Authenticate with gspread
client = gspread.authorize(creds)

# Extract the sheet ID from the URL
# url = 'https://docs.google.com/spreadsheets/d/1eYejJ1ywhqlTF1KIGGmTTAzpwD6TuyvBPSqdsfHHCsA/edit?gid=0#gid=0'
# sheet_id = url.split('/')[-2]

# Open the sheet by its ID
sheet = client.open_by_key("1eYejJ1ywhqlTF1KIGGmTTAzpwD6TuyvBPSqdsfHHCsA").sheet1

data = ["full_name", "email", "idea_title", "industry", "description", "impact", "usp"]

# data = sheet.get_all_records()
def  append_row(data):
    sheet.append_row(data)
    return True
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import sqlite3
from datetime import datetime


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID = "1li1bBj7I7fLTEEIZhbp9gcCNU8mMjOKHVAJ0JJvwtxU"

def get_google_sheet_data():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('appname\credential.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        current_date = datetime.now().strftime("%d/%m/%Y")
        range_name = f"'{current_date}'!A2:K5"  # Update the range to capture all rows
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_name).execute()
        values = result.get('values')
        
        # Initialize an empty list to store the data in dictionary format
        data_list = []

        # Assuming the first row contains column headers
        if values:
            headers = values[0]
            for row in values[1:]:  # Start from the second row
                data_dict = {}
                for i, header in enumerate(headers):
                    data_dict[header] = row[i] if i < len(row) else ''  # Handle missing data
                data_list.append(data_dict)

        # Return the list of dictionaries
        return data_list

    except HttpError as err:
        print(f'An error occurred: {err}')

# Example usage:
data = get_google_sheet_data()
print(data)  # This will print the retrieved data as a list of dictionaries

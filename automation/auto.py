import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from PIL import Image
import requests
from io import BytesIO

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1dBPUuzZy6cRKYqsdlMYxILs3ryrYLgzePcoE85j4UcM"
SAMPLE_RANGE_NAME = "Sponsors!F3:F3"

domain = 'http://127.0.0.1:8000'


speaker_types = {
    'Talks': 'T',
    'Panels': 'P',
    'Career Circles': 'CC',
    'Mentorship': 'M',
    'Workshops': 'W',
}

days = {
    'Day 1 , July 5': '2024-07-05',
    'Day 2 , July 6': '2024-07-06',
    'Day 3 , July 7': '2024-07-07',
}

stages = {
    'Primary': 'P',
    'Secondary': 'S',
    'Workshop': 'W',
    'Mentorship': 'M',
    'Career Circles': 'CC',
}


community_type = {
    'Host': 'H',
    'Main': 'M',
}


def download_show_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    # get the image name from the url
    local_image_path = image_url.split("/")[-1]
    image.save(local_image_path)
    return local_image_path


def edit_sheet(sheet_id, range_name, creds, values):
    service = build("sheets", "v4", credentials=creds)
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption="RAW",
        body={"values": values},
    ).execute()

# all done
# the remaining is interacting with the api


def sheetHandler(sheet_name, row):
    if sheet_name == "Sponsors":
        pass
    if sheet_name == "Communities Partners":
        pass
    if sheet_name == "Partners":
        pass
    if sheet_name == "Vips":
        pass
    if sheet_name == "Mentors":
        pass
    if sheet_name == "Speakers":
        pass
    if sheet_name == "Emails":
        pass
    if sheet_name == "Host & Main Communities":
        pass


def read_sheet(sheet_id, range_name, creds):
    data = []
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=sheet_id, range=range_name)
        .execute()
    )
    values = result.get("values", [])

    if not values:
        print("No data found.")
        return
    data = []
    for row in values:
        data.append(row)
        sheetHandler(range_name.split("!")[0], row)
    return values.__len__()

    # for row in values:
    #     path = download_show_image(row[0])
    #     with open(path, "rb") as image:
    #         file = {'image': image}
    #         response = requests.post(
    #             "http://127.0.0.1:8000/api/image/", files=file, data={"model": "sponsors", "name": "test_sponsor"})
    #     if response.status_code == 200:
    #         print("Image uploaded successfully")


def get_sheet_last_row(sheet_id, range_name, creds):
    service = build("sheets", "v4", credentials=creds)
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=sheet_id, range=range_name)
        .execute()
    )
    values = result.get("values", [])
    if not values:
        print("No data found.")
        return
    return values[0][0]


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            print(flow)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # read_sheet(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, creds)
    sheets = ['Sponsors', 'Communities Partners', 'Partners', 'Vips', 'Mentors', 'Speakers', 'Emails',
              'Host & Main Communities ']
    for sheet in sheets:
        SAMPLE_RANGE_NAME = f"{sheet}!N2:N2"
        last_read = int(get_sheet_last_row(
            SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, creds))

        SAMPLE_RANGE_NAME = f"{sheet}!A{last_read + 1}:K"
        last_record = read_sheet(
            SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, creds)
        if last_record == None:
            last_record = 0
        SAMPLE_RANGE_NAME = f"{sheet}!N2:N2"
        edit_sheet(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME,
                   creds, [[last_record + last_read]])
        break


if __name__ == "__main__":
    main()

worksheet = "JFlab.ca Lab Member Information"

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

WORKBOOK = "JFlab.ca Lab Member Information"


def download_data(credentials_path):
    """Download data using the Google Sheets API"""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_path, scope
    )
    client = gspread.authorize(credentials)

    worksheet = client.open(WORKBOOK).get_worksheet(0)
    sheet_values = worksheet.get_all_values()

    print(f"Downloading: {worksheet.title}")
    with open("./_data/all_members.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(sheet_values)

    print("Updated ./_data/all_members.csv")

if __name__ == "__main__":
    import sys
    credentials_path = sys.argv[-1]
    download_data(credentials_path)

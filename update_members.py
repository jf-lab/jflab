worksheet = "JFlab.ca Lab Member Information"

import csv
import yaml
import gspread
from oauth2client.service_account import ServiceAccountCredentials

WORKBOOK = "jflab.ca"


def download_data():
    """Download data using the Google Sheets API"""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )
    client = gspread.authorize(credentials)

    worksheet = client.open(WORKBOOK).get_worksheet(0)
    sheet_values = worksheet.get_all_values()

    print(f"Downloading: {worksheet.title}")
    with open("./_data/all_members.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(sheet_values)


def generate_site():
    """Generate _data/members.yml in local directory"""
    print("Process data")

    csv = csv.read("./_data/all_members.csv")
    File.write('test.yaml', csv.to_yaml)
    pp YAML.load_file('test.yaml')

    with open(") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    output = template.render(data=data)

    with open("./_data/all_members.yml", "w") as f:
        f.write(output)




if __name__ == "__main__":
    download_data()
    generate_site()
    deploy_site()
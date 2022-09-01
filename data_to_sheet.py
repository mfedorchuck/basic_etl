from oauth2client.service_account import ServiceAccountCredentials
import gspread

SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


def write_data(target_note, doc_name='test sheet'):
    # Auth with Service Account Key
    client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE))

    sheet = client.open(doc_name)
    worksheet = sheet.worksheet('Sheet1')

    worksheet.append_row(['currency ISO', 'currency ISO', 'Buy rate', 'Sell rate'])
    worksheet.append_row([target_note['currencyCodeA'], target_note['currencyCodeB'],
                          target_note['rateBuy'], target_note['rateSell']])


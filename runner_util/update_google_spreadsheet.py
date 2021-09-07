import httplib2
from datetime import datetime
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetsHandler:

    def __init__(self, credentials_file, spreadsheet_id, sheet_id, test_mapper):
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.sheet_id = sheet_id
        self.tests_mapper = test_mapper

        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, [
            'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        self.http_auth = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('sheets', 'v4', http=self.http_auth)

    def _set_column_header_styling(self, last_column_index):
        denominator = 255
        body = {
            'requests': [
                {
                    'repeatCell': {
                        'range': {
                            'sheetId': 860745136,
                            'startColumnIndex': last_column_index,
                            'endColumnIndex': last_column_index + 1,
                            'endRowIndex': 2,
                        },
                        'cell': {
                            'userEnteredFormat': {
                                'horizontalAlignment': 'LEFT',
                                'verticalAlignment': 'MIDDLE',
                                'wrapStrategy': 'WRAP',
                                'textFormat': {'bold': True},
                                'backgroundColor': {
                                    'red': 153 / denominator,
                                    'green': 153 / denominator,
                                    'blue': 153 / denominator
                                },
                            }
                        },
                        'fields': '*'
                    }
                },

            ]
        }

        self.service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body=body
        ).execute()

    @staticmethod
    def cell_styling(start_column_index, start_row_index, status):

        denominator = 255
        background_color = {'red': 183 / denominator, 'green': 224 / denominator, 'blue': 205 / denominator}
        if status == 'Fail':
            background_color = {'red': 244 / denominator, 'green': 198 / denominator, 'blue': 195 / denominator}

        request = {
            'repeatCell': {
                'range': {
                    'sheetId': 860745136,
                    'startColumnIndex': start_column_index - 1,
                    'endColumnIndex': start_column_index,
                    'startRowIndex': start_row_index,
                    'endRowIndex': start_row_index + 1,
                },
                'cell': {
                    'userEnteredFormat': {
                        'horizontalAlignment': 'CENTER',
                        'verticalAlignment': 'MIDDLE',
                        'wrapStrategy': 'WRAP',
                        'textFormat': {'bold': True},
                        'backgroundColor': background_color,
                    }
                },
                'fields': '*'
            }
        }

        return request

    def _set_cells_styling(self, requests):
        self.service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={'requests': requests}
        ).execute()

    def _set_column_headers(self, new_column_index, **kwargs):
        text = ''
        order = ['date', 'Android', 'iOS', 'browser', 'version', 'build']
        for item in order:
            value = kwargs.get(item)
            if value:
                text += f'{item.capitalize()}: {value} '

        self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                'valueInputOption': 'USER_ENTERED',
                'data': [
                    {
                        'range': f'Regression scope!R1C{new_column_index}:R1000C{new_column_index}',
                        'majorDimension': 'ROWS',
                        'values': [['Status'], [text]]
                    }
                ]
            }
        ).execute()

    def _batch_update(self, updates):
        result = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                'valueInputOption': 'USER_ENTERED',
                'data': updates
            }
        ).execute()
        return result

    def get_spreadsheet_headers(self, range_='Regression scope!1:2', dimension='ROWS'):
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=range_,
            majorDimension=dimension
        ).execute()
        return values

    def batch_update(self, test_results, run_info):
        headers = self.get_spreadsheet_headers().get('values')
        need_new_column, indexes = self.header_checker(headers=headers, **run_info)
        last_column_index = len(headers[0]) if need_new_column else indexes[0] + 1
        new_column_index = last_column_index + 1
        column_added = False

        if need_new_column:
            self._set_column_header_styling(last_column_index=last_column_index)
            self._set_column_headers(new_column_index=new_column_index, **run_info)
            column_added = True

        dirty_aa_column = self.get_spreadsheet_headers(range_='Regression scope!A:A',
                                                       dimension='COLUMNS').get('values')[0]
        clean_aa_column = self.clear_data(data=dirty_aa_column)

        updates = []
        requests = []
        for test, status in test_results.items():
            test_short_name = self.tests_mapper.get(test)
            try:
                row = clean_aa_column.index(test_short_name)
                status = 'Pass' if status else 'Fail'
                column = new_column_index if column_added else last_column_index
                update = {
                    'range': f'Regression scope!R{row + 1}C{column}',
                    'majorDimension': 'ROWS',
                    'values': [[status]]
                }
                request = self.cell_styling(start_column_index=column, start_row_index=row, status=status)
                updates.append(update)
                requests.append(request)
            except ValueError as e:
                print(f"ValueError, reason: {e}")
            except Exception as e:
                print(f'Unhandled exception: {e}')

        self._set_cells_styling(requests=requests)
        self._batch_update(updates=updates)

    @staticmethod
    def clear_data(data):
        return [item.strip() for item in data]

    @staticmethod
    def header_checker(headers, **kwargs):
        need_new_columns = True
        indexes = []
        if len(headers[1]) >= 10:
            for index, item in enumerate(headers[1][9:]):
                check_list = []
                for key, value in kwargs.items():
                    if f'{key.capitalize()}: {value}' in item:
                        check_list.append(True)
                    else:
                        check_list.append(False)
                if all(check_list):
                    indexes.append(index + 9)
                    break
            if indexes:
                need_new_columns = False
        return need_new_columns, indexes

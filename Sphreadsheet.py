import time
import gspread

class SphreadSheet(object):
    def __init__(self, settings):
        self.settings = settings
        gc = gspread.service_account(filename=settings['api'])
        self.wb = gc.open(settings['worksheet'])

    def get_column(self, sheetname, column, from_row):
        ws = self.wb.worksheet(sheetname)
        columns = ws.col_values(column)[from_row:]
        return columns
    
    def write_column(self, sheetname, column_name, content, shift=2):
        ws = self.wb.worksheet(sheetname)

        for (i, item) in enumerate(content):
            ws.update_acell(column_name + str(i + shift), item)
            time.sleep(1/2)
        

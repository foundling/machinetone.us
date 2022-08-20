import gspread

service_account = gspread.service_account(filename='service_account.json')

sheet = service_account.open('Website Updates Database')
worksheet = sheet.worksheet('Artist')

print(worksheet.row_count)
print(worksheet.col_count)


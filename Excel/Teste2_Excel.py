import xlwt
    
def get_database(rows):
    collection = []
    for n in range(rows):
        collection.append({
            'id': n,
            'name': 'Luis'
            })
    return collection

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Users')

worksheet.write(0, 0, u'ID')
worksheet.write(0, 1, u'Nome')

users = get_database(1)
for i, user in enumerate(users):
    worksheet.write(i + 1, 0, user['id'])
    worksheet.write(i + 1, 1, user['name'])

workbook.save('user.xls')


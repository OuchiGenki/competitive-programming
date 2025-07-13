
'''
    sheet_border.py
    purpose: read xlsx and set border automatically
'''

import openpyxl as xl
from openpyxl.styles.borders import Border, Side

from itertools import product

def check(v):
    flag = True
    if not (v[0] <= v[1] <= v[2]):
        flag = False
    if not (v[3] <= v[4]):
        flag = False
    if not (v[0] <= v[3] <= v[5]):
        flag = False
    if not (v[1] <= v[4]):
        flag = False
    return flag        


def show(v):
    v = list(map(str, v))
    idx = 0
    print('-'*5)
    for l in [3, 2, 1]:
        print('|'.join(v[idx:idx+l]))
        print('-'*l)
        idx += l
    print()


cnt = 0
for v in product([1, 2, 3], repeat=6):
    if check(v):
        write(v)
        print()
        cnt += 1
print(cnt)


def write(v):
    


# openpyxlをimport
import openpyxl

# 書き込むセルを取得
# ブックを変数に格納
write_wb = openpyxl.load_workbook("Books/Book_write.xlsx")
# シートを変数に名前で格納
write_ws = write_wb["Sheet1"]
# cはセル番地でA1のセルを取得する
c = write_ws["A1"]
# c2は行列番号でA2のセルを取得する
c2 = write_ws.cell(1, 2)
# 変数cにvalueを付けて値を設定する
c.value = "A1です"
c2.value = "B1です"

# Book_write.xlsxに上書保存
write_wb.save("Books/Book_write.xlsx")

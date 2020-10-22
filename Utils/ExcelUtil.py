"""
Excel工具类
"""
import xlrd


def get_head(path):
    """获取标题行"""
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    head_data = table.row_values(0)
    return head_data


def get_rows_by_date(path, date):
    """获取行根据日期"""
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    row_data = None
    for row_num in range(table.nrows):
        if row_data is not None:
            break
        row_val = table.row_values(row_num)
        for col_num in range(table.ncols):
            if row_num > 0 and col_num == 0:
                first_val = row_val[col_num]
                if first_val is not None and first_val != '':
                    begin = first_val.find('（')
                    end = first_val.rfind('）')
                    excel_date = first_val[begin + 1:end]
                    if excel_date == date:
                        row_data = row_val
                    else:
                        break
    return row_data


if __name__ == '__main__':
    path = 'D:/巡检排班.xlsx'
    print(get_head(path))
    print(get_rows_by_date(path, '11.1'))

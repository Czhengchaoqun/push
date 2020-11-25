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
    # 获取合并的单元格
    merged = merge_cell(table)
    row_data = None
    for row_num in range(1, table.nrows):
        if row_data is not None:
            break
        row_val = table.row_values(row_num)
        if len(row_val) <= 0:
            continue
        first_val = row_val[0]
        if first_val is not None and len(first_val) > 0:
            begin = first_val.find('（')
            end = first_val.rfind('）')
            excel_date = first_val[begin + 1:end]
            if excel_date == date:
                for index in range(len(row_val)):
                    if merged.get((row_num, index)):
                        # 这是合并后的单元格，需要重新取一次数据
                        row_val[index] = table.cell_value(*merged.get((row_num, index)))
                row_data = row_val
            else:
                continue
    return row_data


def merge_cell(sheet):
    rt = {}
    if sheet.merged_cells:
        # exists merged cell
        for item in sheet.merged_cells:
            for row in range(item[0], item[1]):
                for col in range(item[2], item[3]):
                    rt.update({(row, col): (item[0], item[2])})
    return rt


if __name__ == '__main__':
    path = 'D:/巡检排班.xlsx'
    print(get_head(path))
    print(get_rows_by_date(path, '11.1'))

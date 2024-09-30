import csv
import sql_utils

# 打开 CSV 文件进行读取
with open('source.csv', mode='r', newline='', encoding='utf-8') as file:
    # 创建一个 CSV 读取器对象
    csv_reader = csv.reader(file)

    # 读取 CSV 文件的标题行（可选）
    headers = next(csv_reader)
    # print("Headers:", headers)

    alter_result = []
    update_result = []


    def build_sql(table_name, column_name, column_length):
        sql = 'alter table {} MODIFY {} VARCHAR2({});'.format(table_name, column_name, column_length)
        return sql


    # 遍历 CSV 文件中的每一行
    for row in csv_reader:
        # 处理每一行的数据
        # print("Row:", row)
        table_name = row[1]
        table_column = row[2]
        column_length = row[4]

        alter_result.append(sql_utils.build_alter_sql(table_name, table_column, column_length))
        update_result.append(sql_utils.build_update_sql(table_name, table_column))

    with open("alter_result.txt", "w", encoding="utf-8") as result_file:
        for item in alter_result:
            result_file.write(f"{item}\n")

    with open("update_result.txt", "w", encoding="utf-8") as update_file:
        for item in update_result:
            update_file.write(f"{item}\n")

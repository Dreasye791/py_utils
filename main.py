import csv
import sql_utils

with open('source.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # 读取 CSV 文件的标题行
    # headers = next(csv_reader)

    alter_result = []
    update_result = []

    for row in csv_reader:
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

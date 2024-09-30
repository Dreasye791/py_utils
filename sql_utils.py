def build_update_sql(table_name, column_name) -> str:
    """
    创建更新表字段的语句
    :param table_name:
    :param column_name:
    :return:
    """
    sql = 'update {} set {} = rtrim({});'.format(table_name, column_name, column_name)
    return sql


def build_alter_sql(table_name, column_name, column_length) -> str:
    """
    创建修改表字段的语句
    :param table_name:
    :param column_name:
    :param column_length:
    :return:
    """
    sql = 'alter table {} MODIFY {} VARCHAR2({});'.format(table_name, column_name, column_length)
    return sql

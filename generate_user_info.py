import pymysql

from generate_random_id import generate_random_id
from sqls import *

pay_database = {
    'port': 3306,
}

pay_connection = pymysql.connect(**pay_database)
pay_cursor = pay_connection.cursor(pymysql.cursors.DictCursor)

dms_database = {
    'port': 3306,
}

dms_connection = pymysql.connect(**dms_database)
dms_cursor = dms_connection.cursor(pymysql.cursors.DictCursor)


def get_user_in_pay_db():
    pay_cursor.execute(get_all_user_in_pay)
    results = pay_cursor.fetchall()
    for result in results:
        print(result)
    pay_cursor.close()


def insert_user_into_pay_db(user_number, coin, user_name, user_uuid):
    pay_cursor.execute(
        insert_user,
        (user_number, coin, user_name, user_uuid)
    )
    pay_connection.commit()


def get_user_in_dms_db():
    dms_cursor.execute(get_all_user_in_dms)
    results = dms_cursor.fetchall()
    return results

def get_user_by_uuid_in_pay_db(uuid):
    pay_cursor.execute(
        find_user_by_uuid_in_pay,
        uuid
    )
    return pay_cursor.fetchall()


if __name__ == '__main__':
    users = get_user_in_dms_db()

    for user in users:
        uuid = generate_random_id()
        while get_user_by_uuid_in_pay_db(uuid):
            uuid = generate_random_id()

        insert_user_into_pay_db(user["number"], 20000, user["name"], uuid)

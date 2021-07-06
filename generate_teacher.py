import pymysql

from generate_random_id import generate_random_id, generate_easy_password
from sqls import *
from teacher_info import teachers

pay_database = {
    'port': 3306,
}

pay_connection = pymysql.connect(**pay_database)
pay_cursor = pay_connection.cursor(pymysql.cursors.DictCursor)


def insert_user_into_pay_db(user_number, coin, user_name, user_uuid):
    pay_cursor.execute(
        insert_user,
        (user_number, coin, user_name, user_uuid)
    )
    pay_connection.commit()


def insert_teacher_into_pay_db(id, name, number, password):
    pay_cursor.execute(
        insert_teacher,
        (id, name, number, password)
    )
    pay_connection.commit()


def get_user_by_uuid_in_pay_db(uuid):
    pay_cursor.execute(
        find_user_by_uuid_in_pay,
        uuid
    )
    return pay_cursor.fetchall()


if __name__ == '__main__':
    for teacher in teachers:
        uuid = generate_random_id()
        while get_user_by_uuid_in_pay_db(uuid):
            uuid = generate_random_id()

        insert_user_into_pay_db(teacher["number"], 100000, teacher["name"], uuid)
        insert_teacher_into_pay_db(teacher["number"], teacher["name"], teacher["number"], generate_easy_password())

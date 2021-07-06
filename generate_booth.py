import pymysql

from booth_info import booths
from generate_random_id import generate_random_id, generate_easy_password
from generate_random_password import generate_random_password
from sqls import *

pay_database = {
    'port': 3306,
}

pay_connection = pymysql.connect(**pay_database)
pay_cursor = pay_connection.cursor(pymysql.cursors.DictCursor)


def insert_booth_into_pay_db(booth_id, booth_name, coin, password, total_coin):
    print(booth_id, booth_name, coin, password, total_coin)
    pay_cursor.execute(
        insert_booth,
        (booth_id, booth_name, coin, password, total_coin)
    )
    pay_connection.commit()


if __name__ == '__main__':
    for booth in booths:
        password = generate_easy_password()
        insert_booth_into_pay_db(booth['booth_id'], booth['booth_name'], 0, password, 0)

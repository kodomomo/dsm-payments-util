get_all_user_in_pay = "SELECT * FROM tbl_user;"
get_all_user_in_dms = "SELECT * FROM student;"
find_user_by_uuid_in_pay = "SELECT * FROM tbl_user WHERE 'user_uuid' = %s"
insert_user = "INSERT INTO tbl_user(user_number, coin, user_name, user_uuid) VALUE (%s, %s, %s, %s)"
insert_teacher = "INSERT INTO tbl_teacher(id, name, number, password) VALUE (%s, %s, %s, %s)"
insert_booth = "INSERT INTO tbl_booth(booth_id, booth_name, coin, password, total_coin) VALUE (%s, %s, %s, %s, %s)"
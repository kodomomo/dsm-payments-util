get_all_user_in_pay = "SELECT * FROM tbl_user;"
get_all_user_in_dms = "SELECT * FROM student;"
find_user_by_uuid_in_pay = "SELECT * FROM tbl_user WHERE 'user_uuid' = %s"
insert_user = "INSERT INTO tbl_user(user_number, coin, user_name, user_uuid) VALUE (%s, %s, %s, %s)"
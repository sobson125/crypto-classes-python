from Saving_Passwords.src.DBController import DBController
from Saving_Passwords.src.Password_Utils import PasswordUtils

if __name__ == "__main__":
    db_controller = DBController()
    db_controller.add_user('damian', '123$123qwe')
    damian = db_controller.get_user('damian')
    print(PasswordUtils.verify_password(stored_password=damian[2], salt=damian[1], input_password="123$123qwe"))

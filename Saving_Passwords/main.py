from Saving_Passwords.src.DBController import DBController

if __name__ == "__main__":
    db_controller = DBController()
    db_controller.add_user('damian', '123$123qwe')
    damian = db_controller.get_user('damian')
    print(damian)

from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register_validate(self, user_info):
        errors = []
        success= []

        if not user_info['name']:
            errors.append("Name cannot be blank")
        elif len(user_info['name']) < 3:
            errors.append("Name must have at least 3 letters")
        if not user_info['username']:
            errors.append("Username cannot be blank")
        elif len(user_info['username']) < 3:
            errors.append("Username must have at least 3 letters")
        if not user_info['password']:
            errors.append("Password cannot be blank")
        elif len(user_info['password']) < 8:
            errors.append("Password must have at least 8 characters")
        if not user_info['confirm']:
            errors.append("Confirm cannot be blank")
        elif not user_info['password'] == user_info['confirm']:
            errors.append("Password and confirm don't match")
        if not user_info['date']:
            errors.append("Must fill in date")

        if errors:
            return {"status": False, "errors": errors}

        else: 
            hashed_pw = self.bcrypt.generate_password_hash(user_info['password'])
            register_query = "INSERT INTO users (name, username, pw_hash, date_hired) VALUES (%s, %s, %s, %s)"
            register_data = [user_info['name'], user_info['username'], hashed_pw, user_info['date']]
            self.db.query_db(register_query, register_data)
            success.append("Successfully Registered!")

            return {"status": True, "success": success}

    def login_validate(self, login_info):
        errors = []

        user_query = "SELECT * FROM users where username = %s LIMIT 1"
        user_data = [login_info['username']]
        password = login_info['password']
        user = self.db.query_db(user_query, user_data)
        print user

        try:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                return {"status": True, "user": user[0]}
            else:
                errors.append("Password is incorrect")
                return {"status": False, "errors": errors}

        except:
            errors.append("Username is not valid")
            return {"status": False, "errors": errors}





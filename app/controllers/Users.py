from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        try:
            session['reg_or_log']
        except:
            session['reg_or_log'] = ''

        return self.load_view('index.html', message=session['reg_or_log'])

    def register(self):

    	user_info = {
    		"name": request.form['name'],
    		"username": request.form['username'],
    		"password": request.form['password'],
    		"confirm": request.form['confirm'],
    		"date": request.form['date']
    	}

    	register_status = self.models['User'].register_validate(user_info)

        if register_status['status'] == True:
            session['reg_or_log'] = "register"
            for message in register_status['success']:
                flash(message)

        else: 
            session['reg_or_log'] = "register"
            for message in register_status['errors']:
                flash(message)

        return redirect('/')

    def login(self):

        login_info = {
            "username": request.form['username'],
            "password": request.form['password']
        }

        login_status = self.models['User'].login_validate(login_info)
        print login_status

        if login_status['status'] == True:
            session['username'] = login_status['user']['username']
            session['user_id'] = login_status['user']['id']
            return redirect('/items/dashboard')
        else: 
            session['reg_or_log'] = "login"
            for message in login_status['errors']:
                flash(message)
            return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')

    


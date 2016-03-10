from system.core.controller import *

class Items(Controller):
    def __init__(self, action):
        super(Items, self).__init__(action)
        
        self.load_model('Item')

    def dashboard(self):
        user_id = session['user_id']
        myItems = self.models['Item'].get_my_items(user_id)
        otherItems = self.models['Item'].get_other_items(user_id)
        return self.load_view('dashboard.html', username=session['username'], myItems=myItems, otherItems=otherItems)

    def create(self):
        return self.load_view('create.html')

    def add(self):
        
        item_info = {
            "item": request.form['item'],
            "user_id": session['user_id']
        }

        item_status = self.models['Item'].item_validate(item_info)

        if item_status['status'] == True:
            return redirect('/items/dashboard')
        else:
            for message in item_status['errors']:
                flash(message)
            return redirect('/items/create')

    def show(self, item_id):
        item = self.models['Item'].get_item_by_id(item_id)
        users = self.models['Item'].get_users_by_item_name(item[0]['item'])
        return self.load_view('item.html', item=item, users=users)

    def delete(self, item_id):
        info = {
            "user_id": session['user_id'],
            "item_id": item_id
        }

        self.models['Item'].delete_item(info)
        return redirect('/items/dashboard')

    def add_wishlist(self, item_id):
        info = {
            "user_id": session['user_id'],
            "item_id": item_id
        }

        self.models['Item'].add_wishlist(info)
        return redirect('/items/dashboard')


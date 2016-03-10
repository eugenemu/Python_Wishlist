from system.core.model import Model

class Item(Model):
    def __init__(self):
        super(Item, self).__init__()

    def item_validate(self, item_info):
        errors = []

        if not item_info['item']:
            errors.append("Item cannot be blank")
        elif len(item_info['item']) < 3:
            errors.append("Item must be longer than 3 characters")
        
        if errors:
            return {"status": False, "errors": errors}

        else: 
            item_query = "INSERT INTO items (item, user_id, created_at) VALUES (%s, %s, now())"
            item_data = [item_info['item'], item_info['user_id']]
            self.db.query_db(item_query, item_data)

            item_id_query = "SELECT id FROM items ORDER BY id DESC LIMIT 1"
            wishlist_id = self.db.query_db(item_id_query)
            
            wishlist_query = "INSERT INTO wishlist (user_id, item_id) VALUES (%s, %s)"
            wishlist_data = [item_info['user_id'], wishlist_id[0]['id']]
            self.db.query_db(wishlist_query, wishlist_data)
            
            return {"status": True}

    def get_my_items(self, user_id):

        query = "SELECT wishlist.user_id, username, items.id, items.user_id, item, DATE_FORMAT(items.created_at, '%b %D %Y') as timestamp FROM wishlist JOIN items on items.id = wishlist.item_id JOIN users on items.user_id = users.id WHERE wishlist.user_id = %s"
        user_id = [user_id]

        return self.db.query_db(query, user_id)

    def get_item_by_id(self, item_id):
        item_query = "SELECT item FROM items WHERE id = %s"
        item_id = [item_id]
        return self.db.query_db(item_query, item_id)

    def get_users_by_item_name(self, item):
        users_query = "SELECT username, DATE_FORMAT(items.created_at, '%b %D %Y') as timestamp FROM items JOIN users on users.id = items.user_id WHERE item = %s"
        item = [item]
        return self.db.query_db(users_query, item)

    def get_other_items(self, user_id):
        
        query = "SELECT wishlist.user_id, users.username, items.user_id as item_creator, items.id, item, DATE_FORMAT(items.created_at, '%b %D %Y') as timestamp FROM wishlist JOIN items on items.id = wishlist.item_id JOIN users on items.user_id = users.id WHERE items.id NOT IN (SELECT wishlist.item_id from wishlist WHERE wishlist.user_id = %s)"
        user_id = [user_id]
        return self.db.query_db(query, user_id)

    def delete_item(self, info):
        query = "DELETE FROM wishlist WHERE item_id = %s and user_id = %s"
        data = [info['item_id'], info['user_id']]
        self.db.query_db(query, data)

    def add_wishlist(self, info):
        query = "INSERT INTO wishlist (user_id, item_id) VALUES (%s, %s)"
        data = [info['user_id'], info['item_id']]
        self.db.query_db(query, data)





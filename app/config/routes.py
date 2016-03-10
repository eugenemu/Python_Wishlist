from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/users/register'] = 'Users#register'
routes['POST']['/users/login'] = 'Users#login'
routes['/items/create'] = 'Items#create'
routes['/items/show/<item_id>'] = 'Items#show'
routes['/items/add_wishlist/<item_id>'] = 'Items#add_wishlist'
routes['/items/delete/<item_id>'] = 'Items#delete'
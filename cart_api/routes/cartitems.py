import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseCartItem


# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec


class CartItems:
    def on_get(self, req, resp):
        items = DatabaseCartItem.select()
        itemList = []
        for item in items:
            itemList.append(model_to_dict(item))
        resp.media = itemList
        resp.status = falcon.HTTP_200
   
    def on_post(self, req, resp):
        obj = req.get_media()
        new_item = DatabaseCartItem(
            name=obj.get('name'),
            price=obj.get('price'),
            quantity=obj.get('quantity')
           
        )
        new_item.save()
        resp.media = model_to_dict(new_item)
        resp.status = falcon.HTTP_201


class CartItem:
    def on_get(self, req, resp, item_id):
        cartItem = DatabaseCartItem.get(id=item_id)
        resp.media = model_to_dict(cartItem)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, item_id):
        DatabaseCartItem.delete_by_id(item_id)
        resp.status = falcon.HTTP_204
    
    def on_patch(self, req, resp, item_id):
        obj = req.get_media()
        cartItem = DatabaseCartItem.get(id=item_id)
        cartItem.quantity = obj.get('quantity')
        
        cartItem.save()
        # resp.media = model_to_dict(cartItem)
        resp.status = falcon.HTTP_204

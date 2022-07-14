import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseProducts


class Product:
    def on_get(self, req, resp, product_id):
        product = DatabaseProducts.get(id=product_id)
        resp.media = model_to_dict(product)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, product_id):
        DatabaseProducts.delete_by_id(product_id)
        resp.status = falcon.HTTP_204


# Excercise 2:
# Products route should respond to GET and POST requests
# GET products returns a list of every product in the database
# POST products creates a product and returns the data it created


class Products:
    # def on_get(self, req, resp):
    def on_get(self, req, resp):
        resp.media = []
        products = DatabaseProducts.select()
        for product in products:
            resp.media.append(model_to_dict(product))
        resp.status = falcon.HTTP_200

    # def on_post(self, req, resp):
    def on_post(self, req, resp):
        new_product = req.get_media()
        new_model = DatabaseProducts(
            name=new_product["name"],
            description=new_product["description"],
            image_url=new_product["image_url"],
            price=new_product["price"],
            is_on_sale=new_product["is_on_sale"],
            sale_price=new_product["sale_price"],
        )
        new_model.save()
        resp.media = model_to_dict(new_model)
        resp.status = falcon.HTTP_201

import graphene
from graphene import ObjectType, String, Int
from stocks.schemas.product import Product
from db import get_redis_conn

class Query(ObjectType):       
    product = graphene.Field(Product, id=String(required=True))
    stock_level = Int(product_id=String(required=True))
    quantity = graphene.Int()
    name = graphene.String()
    sku = graphene.String()
    price = graphene.Float()
    
    def resolve_product(self, info, id):
        """ Create an instance of Product based on stock info for that product that is in Redis """
        redis_client = get_redis_conn()
        product_data = redis_client.hgetall(f"stock:{id}")
        quantite_b = product_data.get("quantity")
        nom_b = product_data.get("name")
        sku_b = product_data.get("sku")
        price_b = product_data.get("price")

        if product_data:
            return Product(
                id=id,
                name=nom_b,
                quantity=int(quantite_b),
                sku=sku_b,
                price=price_b,
            )
    
    def resolve_stock_level(self, info, product_id):
        """ Retrieve stock quantity from Redis """
        redis_client = get_redis_conn()
        quantity = redis_client.hget(f"stock:{product_id}", "quantity")
        return int(quantity) if quantity else 0
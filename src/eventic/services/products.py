from src.common.service import BaseService
from src.eventic.models.products import Product


class ProductService(BaseService):
    model = Product

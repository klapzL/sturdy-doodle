from src.common.service import BaseService
from src.app.models.products import Product


class ProductService(BaseService):
    model = Product

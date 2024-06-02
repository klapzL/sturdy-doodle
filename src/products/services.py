from src.common.service import BaseService
from src.products.models import Product


class ProductService(BaseService):
    model = Product

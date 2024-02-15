"""The pydantic models for the project."""
import decimal
from typing import Dict
from pydantic import BaseModel, condecimal, conint
import constants


class Product(BaseModel):
    """A product for sale on the website."""
    sku: str
    name: str
    description: str = ''
    price: condecimal(ge=decimal.Decimal('0'), decimal_places=2)
    image: str = None

    def get_formatted_price(
            self,
            currency_symbol: str = constants.CURRENCY_SYMBOL) -> str:
        """Get the price rounded to 2 dp as a string with the currency."""
        return f'{currency_symbol}{self.price:.2f}'


class BasketProduct(BaseModel):
    """A summary of products in the basket."""
    product: Product
    quantity: conint(ge=0)

    def get_price(self) -> decimal.Decimal:
        """Get the price for this product."""
        return self.quantity * self.product.price

    def get_formatted_price(
            self,
            currency_symbol: str = constants.CURRENCY_SYMBOL) -> str:
        """Get the price rounded to 2 dp as a string with the currency."""
        return f'{currency_symbol}{self.get_price():.2f}'


class Basket(BaseModel):
    """The content of a user's basket."""
    products: Dict[str, BasketProduct] = {}

    def get_total_price(self) -> decimal.Decimal:
        """Get the total price of the basket."""
        total = 0
        for product in self.products.values():
            total += product.get_price()
        return total

    def get_formatted_price(
            self,
            currency_symbol: str = constants.CURRENCY_SYMBOL) -> str:
        """Get the price rounded to 2 dp as a string with the currency."""
        return f'{currency_symbol}{self.get_total_price():.2f}'

    def is_empty(self) -> bool:
        """Returns True if the basket is empty, else False."""
        return len(self.products) == 0


class User(BaseModel):
    """A logged-in user of the website."""
    user_id: str
    name: str
    email: str


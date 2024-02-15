
"""The CRUD operations for working with products."""
from typing import Dict, Optional
import models
import products


def get_products() -> Dict[str, models.Product]:
    """Get the products for sale on the website.

    Returns:
        A dictionary where the keys are the product SKUs and the values are
        the products.
    """
    return {p['sku']: models.Product(**p) for p in products.RAW_PRODUCTS}


def get_product(sku: str) -> Optional[models.Product]:
    """Get the product with the sku argument.

    Args:
        sku: the sku of the product

    Returns:
        The product if it exists, else None
    """
    products_dict = get_products()
    return products_dict.get(sku)

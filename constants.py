
"""Constants used throughout the project."""
import os

# By default, this project uses GBP £ as the base currency. To override this,
# update the currency code to one of the supported options here:
# https://support.google.com/analytics/answer/9796179
CURRENCY_CODE = os.environ.get('CURRENCY_CODE', 'USD')
# And set the appropriate currency symbol
CURRENCY_SYMBOL = os.environ.get('CURRENCY_SYMBOL', '$')

from utils import currency_rates

currency = input('Enter code:')

result = currency_rates(currency)
print(f'курс: {result}')




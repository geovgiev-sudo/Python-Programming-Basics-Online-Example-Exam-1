from math import floor, ceil


raketa_price = float(input())
raketa_count = int(input())
sneakers_count = int(input())

sneakers_price = raketa_price * (1 / 6)

raketa_total = raketa_price * raketa_count
sneakers_total = sneakers_price * sneakers_count

misc = (raketa_total + sneakers_total) * 0.20
total = raketa_total + sneakers_total + misc

price_djokovic = total / 8
price_sponsors = total * (7 / 8)

print(f'Price to be paid by Djokovic {floor(price_djokovic)}')
print(f'Price to be paid by sponsors {ceil(price_sponsors)}')







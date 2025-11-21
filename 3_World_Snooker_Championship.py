championship_stage = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_photo = input()
ticket_price = 0

if ticket_type == 'Standard':
    if championship_stage == 'Quarter final':
        ticket_price = 55.50
    elif championship_stage == 'Semi final':
        ticket_price = 75.88
    elif championship_stage == 'Final':
        ticket_price = 110.10

elif ticket_type == 'Premium':
    if championship_stage == 'Quarter final':
        ticket_price = 105.20
    elif championship_stage == 'Semi final':
        ticket_price = 125.22
    elif championship_stage == 'Final':
        ticket_price = 160.66

elif ticket_type == 'VIP':
    if championship_stage == 'Quarter final':
        ticket_price = 118.90
    elif championship_stage == 'Semi final':
        ticket_price = 300.40
    elif championship_stage == 'Final':
        ticket_price = 400

total_price = number_of_tickets * ticket_price

if total_price > 4000:
    total_price *= 0.75

elif 4000 >= total_price > 2500:
    total_price *= 0.90
    if trophy_photo == 'Y':
        photo_price = number_of_tickets * 40
        total_price += photo_price

elif total_price < 2500:
    if trophy_photo == 'Y':
        photo_price = number_of_tickets * 40
        total_price += photo_price

print(f'{total_price:.2f}')
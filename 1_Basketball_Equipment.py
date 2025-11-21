yearly_tax = int(input())

ketzove = yearly_tax * 0.60
ekip = ketzove * 0.80
ball = ekip * 0.25
accessories = ball * 0.20

expenses = yearly_tax + ketzove + ekip + ball + accessories

print(f'{expenses:.2f}')
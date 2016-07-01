'''
use bisection search to calculate the smallest fixed payment needed to pay monthly
in order to pay off the debt in a year.the monthly payment is a multiple of $0.01
'''

balance = 999999
annualInterestRate = 0.18

monthly_interest_rate = annualInterestRate / 12.0
low = balance / 12.0
high = (balance * ((1 + monthly_interest_rate) ** 12)) / 12.0
balanceCopy = balance
epsilon = 0.02

while abs(balance) > epsilon:
    balance = balanceCopy
    fixed = (low + high) / 2.0
    for i in range(12):
        balance = (balance - fixed) * (1 + monthly_interest_rate)
    if balance < 0:
        high = fixed
    elif balance > 0:
        low = fixed

print('Lowest Payment: ' + str(round(fixed, 2)))

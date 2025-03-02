# write your code here
import math
import argparse
import sys

parser = argparse.ArgumentParser(description="Annuity calculator")
parser.add_argument("--principal", type=float, help="Principal")
parser.add_argument("--periods", type=int, help="Periods")
parser.add_argument("--interest", type=float, help="Interest")
parser.add_argument("--payment", type=float, help="Payment")
parser.add_argument("--type", type=str, help="Payment type")


args = parser.parse_args()
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
type = args.type
num_args = len(sys.argv) - 1


if not args.type == "annuity" and not args.type == "diff":
    print("Incorrect parameters")

if num_args < 4:
    print("Incorrect parameters")
elif args.principal is None and (args.payment < 0 or args.interest < 0 or args.periods < 0):
    print("Incorrect parameters")
elif args.payment is None and (args.interest < 0 or args.principal < 0 or args.periods < 0):
    print("Incorrect parameters")
elif args.periods is None and (args.interest < 0 or args.payment < 0 or args.principal < 0):
    print("Incorrect parameters")
elif args.interest is None and (args.periods < 0 or args.principal < 0 or args.payment < 0):
    print("Incorrect parameters")




# Calculating the Annuity when user enters annuity option
if args.type == "annuity" and args.interest is None:
    print("Incorrect parameters")
elif args.type == "annuity":
    interest = interest / 100
    if args.payment is None:
        interest = interest / 12
        topHalf = interest * (math.pow(1 + interest, periods))
        bottomHalf = math.pow(1 + interest, periods) - 1
        annuity = principal * (topHalf / bottomHalf)
        totalPaid = math.ceil(annuity) * periods
        overpayment = totalPaid - principal
        print(f'Your monthly payment = {math.ceil(annuity)}!')
        print(f'Overpayment = {overpayment}!')
    elif args.periods is None:
        interest = interest / 12
        numerator = payment
        denominator = payment - interest * principal
        n = math.log(numerator / denominator) / math.log(1 + interest)
        totalPaid = payment * math.ceil(n)
        overpayment = totalPaid - principal
        if n % 12 == 0:
            years = n // 12
            print(f'It will take {years} years to repay this loan!')

        elif n % 12 > 11:
            years = math.ceil(n / 12)
            print(f'It will take {years} years to repay this loan!')
        elif n % 12 > 0:
            years = math.floor(n / 12)
            months = math.ceil(n % 12)
            print(f'It will take {years} years and {months} months to repay this loan!')
        else:
            print(f'It will take {n} years to repay this loan!')
        print(f'Overpayment = {overpayment}!')
    elif args.principal is None:
        interest = interest / 12
        numerator = interest * math.pow(1 + interest, periods)
        denominator = math.pow(1 + interest, periods) - 1
        principal = payment / (numerator / denominator)
        totalPaid = payment * periods
        overpayment = totalPaid - principal
        print(f'Your monthly payment = {math.ceil(principal)}!')
        print(f'Overpayment = {overpayment}!')
# If the user selects differentiated
elif args.type == "diff" and args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff" and args.interest is not None:
    interest = interest / 100
    if args.payment is None:
        interest = interest / 12
        sum = 0
        for i in range(1, periods + 1):
            diffPayment = math.ceil((principal / periods) + interest * (principal - ((principal * (i - 1)) / periods)))
            sum += diffPayment
            print(f'Month {i}: payment is {diffPayment}')
        overpayment = sum - principal
        print(f'Overpayment = {overpayment}!')

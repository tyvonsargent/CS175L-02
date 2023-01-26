# Tyvon Ali Sargent
# CS175L-02
# Stocks


COMMISSION_RATE = float(input("Please enter commission rate as a percent:"))
NUM_SHARES = int(input("Please enter number of shares as a whole number:"))
PURCHASE_PRICE =float(input("Please enter purchase price as a percent:"))
SELLING_PRICE = float(input("Please enter selling price as a percent:"))
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print (f'Amount paid for stock: ${amountPaidForStock:,.2f}')
print (f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print (f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print (f'Commission paid on the sale: ${sellingCommission:,.2f}')
print (f'profit or loss if negative: ${profitOrLoss:,.2f}')

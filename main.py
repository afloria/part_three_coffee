water = input('Write how many ml of water the coffee machine has: ')
milk = input('Write how many ml of milk the coffee machine has: ')
beans = input('Write how many grams of coffee beans the coffee machine has:')
cups_needed = input('Write how many cups of coffee you will need: ')
# Convert input into integer values
w = int(water)
m = int(milk)
b = int(beans)
cn = int(cups_needed)
# Convert ingredients to whole numbers
w //= 200
m //= 50
b //= 15
# Find number of possible coffee cups
pc = min([w,m,b])

if cn == pc:
  print('Yes, I can make that amount of coffee')
elif cn < pc and w != 0 and m != 0 and b != 0:
  print('Yes, I can make that amount of coffee (and even',(pc-cn), 'more than that')
elif cn > pc or w != 0 or m != 0 or b != 0:
  print('No, I can make only',pc,'cups of coffee')




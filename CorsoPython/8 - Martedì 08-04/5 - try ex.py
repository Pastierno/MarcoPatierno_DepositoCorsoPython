a= 0
try:
    print(8/a)
except ZeroDivisionError as e:
    print('Non valida', e)
except:
    print('Non valida')

print('proseguo programma')
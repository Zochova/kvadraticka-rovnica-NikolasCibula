a=int(input('Zadajte číslo pre a='))
b=int(input('Zadajte číslo pre b='))
c=int(input('Zadajte číslo pre c='))
#d=> diskriminant
d=b*b-4*a*c
if 0 > d:
    print('Rovnica má 0 riešení')
else:
    x1=((-b)+sqrt(d)/(2*a))
    x2=((-b)-sqrt(d)/(2*a))
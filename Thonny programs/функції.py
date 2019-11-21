print('\nзвичайна')
def назва_ф():
    print('pp1')
назва_ф()

print('\nз параметрами')
def параметри(x, y, z):
    c = x+y+z
    v = x*y*z
    print(c, v)
параметри(5, 2, 3)

print('\nreturn')
def ідентична_return(a, b, c):
    print('text')                   
    return a*b*c
    print('text')      
          #текст після return НЕ ВИВОДИТЬСЯ, тільки до
print(ідентична_return(5, 2, 3))
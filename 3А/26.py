import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
x = 0
while True:
    try:
        a = input('Введіть число: ')
        if a == '':
            break
        else:
            x += float(a)
            print(x)
    except:
        print('Некоректне значення')
printTimeStamp('Михайлов Сергій')

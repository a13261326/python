duration = int(input("Введите число: "))
days = duration // 86400
hours = duration % 86400 // 3600
minutes = duration % 86400 % 3600 // 60
secs = duration % 86400 % 3600 % 60

if days > 0:
    print(days, ' дней ', hours, ' часов', minutes, ' минут', secs, 'секунд')
elif days == 0 and hours > 0:
    print(hours, ' часов', minutes, ' минут', secs, 'секунд')
elif days == 0 and hours == 0 and minutes>0:
    print(minutes, ' минут', secs, 'секунд')
elif days == 0 and hours == 0 and minutes == 0 and secs>0:
    print(secs, 'секунд')

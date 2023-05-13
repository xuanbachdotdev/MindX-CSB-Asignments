from datetime import datetime

now = datetime.now()

print("Today is %s" % now.strftime('%d/%m/%Y'))
print("Time right now: %s" % now.strftime('%H:%M:%S'))

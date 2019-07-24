performances = {'Ventriloquism':       '9:00am',
                'Snake Charmer':       '12:00pm',
                'Amazing Acrobatics':  '2:00pm',
                'Enchanted Elephants': '5:00pm'}
print(performances)
print("------------Writing above values into file-----------")
schedule_file = open('schedule.txt', 'w')
for key, val in performances.items():
    schedule_file.write(key + " - " + val)
    schedule_file.write("\n")
schedule_file.close()


print('-----------READ FROM FILET---------------')
performances_new = {}
schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.replace("/n", "").split(" - ")
    print(show, time)
    performances_new[show] = time.strip()
schedule_file.close()

print("------------PRINT LIST--------------")
print(performances_new)
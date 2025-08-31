current_time = int(input('Enter current time:\n'))
hours_to_wait = int(input('Enter hours to wait:\n'))
final_time = (current_time + hours_to_wait) % 24
print(f'Alarm will go off at: {final_time}')
      
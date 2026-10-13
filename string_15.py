input_data = input().split()
hour = int(input_data[0])
minute = int(input_data[1])


if hour >= 12:
    period = "PM"
    
    if hour > 12:
        hour -= 12
else:
    period = "AM"
    if hour == 0:
        hour = 12


print(f"{hour:02d} : {minute:02d} {period}")

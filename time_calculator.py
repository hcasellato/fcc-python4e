def add_time(start, duration, weekday = ""):
    time = ((start.split())[0].split(":"))
    time.append((start.split())[1])
    add = duration.split(":")
    week = {"Sunday":1, "Monday":2, "Tuesday":3, "Wednesday":4,
            "Thursday":5, "Friday":6, "Saturday":7}
    week_inv = {value: key for key, value in week.items()}
    # Time transformation
    for i in range(2):
        time[i] = int(time[i])
        add[i] = int(add[i])

    # Hours fixing
    if time[2] == "PM":
        time[0] += 12
    
    # Time Sum!
    final = []
    if time[1] + add[1] >= 60:
        final.append(time[0] + add[0] + 1)
        final.append(time[1] + add[1] - 60)
    else:
        final.append(time[0] + add[0])
        final.append(time[1] + add[1])

    if final[0] >= 24:
        if int(final[0] / 24) == 1:
            final.append("(next day)")
        elif int(final[0] / 24) > 1: 
            final.append(("(%s days later)") % int(final[0] / 24))
        x = int(final[0] / 24)
        final[0] = (final[0] % 24)
    else:
        x = int(final[0] / 24)
        final.append("n/a")

    # Hours unfixing 
    if final[0] > 12:
        final[0] = final[0] - 12
        final.append("PM")
    elif final[0] == 12:
        final[0] = final[0]
        final.append("PM")
    elif final[0] == 0:
        final[0] = 12
        final.append("AM")
    else:
        final.append("AM")
    
    if final[1] < 10:
        final[1] = "0" + str(final[1])
    else:
        final[1] = str(final[1])
    
    if weekday != "":
        w = ((x % 7) + week[weekday.title()]) % 7
        if final[2] == "n/a":
            ans = (str(final[0]) + ":" + final[1] + " %s, " + week_inv[w]) % final[3]
        else:
            ans = (str(final[0]) + ":" + final[1] + " %s, " + week_inv[w] + " " + final[2]) % final[3]
    else:
        if final[2] == "n/a":
            ans = (str(final[0]) + ":" + final[1] + " %s") % final[3]
        else:
            ans = (str(final[0]) + ":" + final[1] + " %s " + final[2]) % final[3]
    return ans

# Ran 12 tests in 0.001s =)
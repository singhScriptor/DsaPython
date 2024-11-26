def weekDays(day):
    name={
        1: 'Monday',
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return name.get(day,"Invalid days")
day=4
print(weekDays(day))
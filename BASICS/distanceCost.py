def distanceCost(distance):
    if distance > 0 and distance <= 100:
        return 5
    elif distance > 100 and distance <= 500:
        return 8
    elif distance > 500 and distance < 1000:
        return 10
    else:
        return 12
d=700
print(distanceCost(d))    



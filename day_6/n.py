f = open("test.in")
times = [7, 15, 30]
distances = [9, 40, 200]
times = [40, 70, 98, 79]
distances = [215, 1051, 2147, 1005]
times = [71530]
distances = [940200]
times = [40709879]
distances = [215105121471005]
a = 1
total = 1
for t, d in zip(times, distances):
    num_win = 0
    for i in range(t+1):
        speed = 0
        speed += i*a
        distance = (t-i)*speed
        # print(distance, speed)
        if distance > d:
            num_win += (t+1) - 2*(i)
            break
            num_win += 1
    # print("w:", num_win)
    total *= num_win

print(total)

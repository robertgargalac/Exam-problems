hour, minutes = input().split(':')
n_choices = input()
n_choices = int(n_choices)
all_trips = []
trip_time_list = []
while n_choices != 0:
    trip_info = input().split(' ')
    all_trips.append(trip_info)
    n_choices -= 1

for trip in all_trips:
    trip_time = int(trip[len(trip) - 1]) + int(trip[len(trip) - 2])
    trip_time_list.append(trip_time)

min_value = min(trip_time_list)
min_index = trip_time_list.index(min(trip_time_list))
detection = False
for i in range(len(trip_time_list)):
    if i == min_index:
        continue
    if min_value == trip_time_list[i]:
        another_min_index = i
        detection = True

if detection:
    if trip_time_list[min_index] == trip_time_list[another_min_index]:

        if all_trips[min_index][0] == 'A':

            best_trip_index = another_min_index
        else:
            best_trip_index = min_index
else:
    best_trip_index = min_index

try:
    h = int(hour)
except:
    lst = hour.split('')
    h = int(lst[1])

try:
    m = int(minutes)
except:
    lst = minutes.split('')
    m = int(lst[1])

arrive_minute = (m + trip_time_list[best_trip_index]) % 60
extra_h = int((m + trip_time_list[best_trip_index]) / 60)
arrive_hour = (h + extra_h) % 24
if arrive_hour < 10:
    arr_hour = '0' + str(arrive_hour)
else:
    arr_hour = str(arrive_hour)
if arrive_minute < 10:
    arr_minute = '0' + str(arrive_minute)
else:
    arr_minute = str(arrive_minute)
print("{} {} {}:{}".format(all_trips[best_trip_index][0], all_trips[best_trip_index][1], arr_hour, arr_minute))





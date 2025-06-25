import numpy as np

daily_temperatures = np.array([
    18.5, 21.2, 23.8, 26.1, 24.7, 22.3, 19.8, 17.2, 20.5, 24.3,
    27.1, 29.4, 31.8, 28.6, 25.9, 23.1, 21.7, 18.9, 22.4, 25.8,
    28.9, 30.7, 33.2, 29.9, 27.4, 24.6, 22.1, 19.5, 23.3, 26.0
])

daily_humidity = np.array([
    72, 68, 65, 61, 58, 63, 69, 75, 71, 64,
    59, 55, 52, 57, 62, 67, 73, 78, 74, 60,
    56, 53, 49, 54, 59, 65, 70, 76, 68, 63
])

daily_rainfall = np.array([
    0.0, 0.0, 1.2, 3.5, 0.0, 0.0, 5.8, 12.3, 2.1, 0.0,
    0.0, 0.0, 0.0, 0.5, 4.2, 8.7, 15.1, 6.9, 1.8, 0.0,
    0.0, 0.0, 0.0, 0.3, 2.9, 6.4, 11.2, 9.8, 3.5, 0.8
])

print("BASIC TEMPERATURE STATS:")

# Average temperature for the month

average = np.mean(daily_temperatures)
print(f"The average temperature of the month was {average:.2f}° C")

# Hottest day and its temperature

hottest_day = (np.argmax(daily_temperatures) + 1)
highest_temp = np.max(daily_temperatures)

print(f"\nThe hotest day of the month was {hottest_day} and the temperature that day was {highest_temp}")

# Coldest day and its temperature

coldest_day = np.argmin(daily_temperatures)
lowest_temp = np.min(daily_temperatures)
print(f"\nThe coldest day of the month was {coldest_day} and the temperature that day was {lowest_temp}")

# Temperature range

temp_range = np.max(daily_temperatures) - np.min(daily_temperatures)

print(f"\nTemperature range : {temp_range:.2f}")

print("\n\nTEMPERATURE CATAGORIES:")

# Hot days

hot_days = []
for temp in daily_temperatures:
    if temp > 28:
        hot_days.append(temp)
hot_days = np.array(hot_days)

print(f"\nHot days : {hot_days}")

# Warm days

warm_days = []
for temp in daily_temperatures:
    if temp < 28 and temp > 22:
        warm_days.append(temp)
warm_days = np.array(warm_days)

print(f"\nWarm days : {warm_days}")

# Cold days

cold_days = []
for temp in daily_temperatures:
    if temp < 22:
        cold_days.append(temp)
cold_days = np.array(cold_days)

print(f"\nCold days : {cold_days}")

print("\n\nHUMIDITY ANALYSIS:")

avg_humidity = np.mean(daily_humidity)
print(f"\nThe average humidity is : {avg_humidity}")

print(f"\nThe day with the highest humidity was {np.argmax(daily_humidity)}")

days = 0
for humidity in daily_humidity:
    if humidity > 70:
        days+= 1

print(f"\n{days} days had humidity above 70%")

print("\n\n RAINFALL INSIGHTS:")

total_rain = np.sum(daily_rainfall)
print(f"\nThe total rainfall for the month was {total_rain:.2f}")

avg_rainfall = np.mean(daily_rainfall)
print(f"\nThe daily average rainfall of the month is {avg_rainfall:.2f}")

print(f"\nDay {np.argmax(daily_rainfall) + 1} had the most rainfall.")

days = 0
for rainfall in daily_rainfall:
    if rainfall > 0.0:
        days+=1

print(f"\n{days} days had any rain.")

days = 0
for rainfall in daily_rainfall:
    if rainfall > 10.0:
        days += 1

print(f"\n{days} days had heavy rainfall.")

print("\n\nWEEKLY BREAKDOWN:\n")

weekly_temp = daily_temperatures[:28].reshape(4,7)

weekly_avg_temp = []
for i in range(len(weekly_temp)):
    weekly_avg_temp.append(round(np.mean(weekly_temp[i]),2))

weekly_avg_temp = np.array(weekly_avg_temp)

for i in range(len(weekly_temp)):
    print(f"The weekly average temperature of week {i+1} is {weekly_avg_temp[i]}°C")

weekly_rainfall = daily_rainfall[:28].reshape(4,7)

total_weekly_rainfall = []

for i in range(len(weekly_rainfall)):
    total_weekly_rainfall.append(round(np.sum(weekly_rainfall[i]),2))

total_weekly_rainfall = np.array(total_weekly_rainfall)

for i in range(len(weekly_rainfall)):
    print(f"The total rainfall of week {i+1} is {total_weekly_rainfall[i]}mm.")

print("\n\n PATTERN RECOGNITION:")

days = 0
for i in range(0,30):
    if (daily_temperatures[i] > 28.00) & (daily_humidity[i] > 65):
        days += 1

print(f"\n{days} days of the month were both hot and humid.")

bool_arr = []
for i in range(len(daily_rainfall)):
    if daily_rainfall[i] > 0.0:
        bool_arr.append(True)
    else:
        bool_arr.append(False)

rainy_day_temp = daily_temperatures[bool_arr]
avg_rainy_day_temp = np.mean(rainy_day_temp)

print(f"\nThe average temperature on rainy days was {avg_rainy_day_temp:.2f} ")

day_no = []
for i in range(0,30):
    if (daily_rainfall[i] > 12) | (daily_temperatures[i] > 30):
        day_no.append(i+1)

day_no = np.array(day_no)

print(f"\nThe days which had extreme weather were {day_no}.")

print("\n" + "="*50)

hottest_3days = np.sort(daily_temperatures)[-3:]

print(f"\nThe 3 hottest days of the month were {hottest_3days}")

early_days = daily_temperatures[:5]
late_days = daily_temperatures[-5:]

avg_early_days = np.mean(early_days)
avg_late_days = np.mean(late_days)

if avg_early_days < avg_late_days:
    print("Getting Warmer!")
elif avg_early_days > avg_late_days:
    print("Getting Cooler!")
else:
    print("Staying about the same.")

daily_changes = daily_temperatures[1:] - daily_temperatures[:-1]

big_swing = np.abs(daily_changes)>5 # np.abs() gives us absolute values

swing_days = np.where(big_swing)[0] + 2 # this [0] is written just to get the array of indices

# # Method 1: Direct indexing (what you're asking about)
# swing_day_indices = np.where(big_swings)[0]

# # Method 2: Unpacking the tuple
# swing_day_indices, = np.where(big_swings)  # Note the comma after the variable

# # Method 3: Using tuple unpacking
# (swing_day_indices,) = np.where(big_swings)

# # All three methods give the same result!

# Get the actual temperature changes for those days
swing_amounts = daily_changes[big_swing]

print(f"The days wiht temperature swings > 5°C for previous day are {swing_days}")

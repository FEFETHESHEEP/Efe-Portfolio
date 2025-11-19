# Record times (in seconds)
WORLD_RECORD = 9.58
NATIONAL_RECORD = 9.85

# Get input for 3 athletes
name1 = input("Enter name of athlete 1: ")
time1 = float(input(f"Enter {name1}'s time: "))

name2 = input("Enter name of athlete 2: ")
time2 = float(input(f"Enter {name2}'s time: "))

name3 = input("Enter name of athlete 3: ")
time3 = float(input(f"Enter {name3}'s time: "))

# Find 1st, 2nd, and 3rd places
if time1 < time2 and time1 < time3:
    first_name, first_time = name1, time1
    if time2 < time3:
        second_name, second_time = name2, time2
        third_name, third_time = name3, time3
    else:
        second_name, second_time = name3, time3
        third_name, third_time = name2, time2

elif time2 < time1 and time2 < time3:
    first_name, first_time = name2, time2
    if time1 < time3:
        second_name, second_time = name1, time1
        third_name, third_time = name3, time3
    else:
        second_name, second_time = name3, time3
        third_name, third_time = name1, time1

else:
    first_name, first_time = name3, time3
    if time1 < time2:
        second_name, second_time = name1, time1
        third_name, third_time = name2, time2
    else:
        second_name, second_time = name2, time2
        third_name, third_time = name1, time1

# Show results
print("\n🏁 Race Results 🏁")
print(f"1st: {first_name} ({first_time}s) 🥇")
print(f"2nd: {second_name} ({second_time}s) 🥈")
print(f"3rd: {third_name} ({third_time}s) 🥉")

# Check for records
print("\n🎉 Record Check 🎉")
if first_time < WORLD_RECORD:
    print(f"{first_name} broke the WORLD RECORD! ({first_time}s)")
elif first_time < NATIONAL_RECORD:
    print(f"{first_name} broke the NATIONAL RECORD! ({first_time}s)")
else:
    print("No records were broken.")

print("\nEnd of Race.")

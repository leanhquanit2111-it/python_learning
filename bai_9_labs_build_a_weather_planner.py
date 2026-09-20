distance_mi = bool() 
is_raining = bool() 
has_bike = bool() 
has_car = bool() 
has_ride_share_app = bool() 
if not distance_mi: 
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False) 
elif distance_mi > 1 and distance_mi <= 6: 
    if has_bike == 1 and is_raining != 0:
        print(True) 
    else: 
        print(False) 
else:
    if has_car == 1 or has_ride_share_app == 1:
        print(True) 
    else: print(False)
            
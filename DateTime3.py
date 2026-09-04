def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    else:
        return 0

def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days

destination = input("Enter your destination city: ")
trip_days = int(input("Enter the number of days/nights: "))

total_hotel = hotel_cost(trip_days)
total_plane = plane_ride_cost(destination)
total_car = rental_car_cost(trip_days)
total_trip_cost = total_hotel + total_plane + total_car

print("Your total cost of the trip is :", total_trip_cost)
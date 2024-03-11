connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
routes_to_rome = 0
total_flight_time = 0

for connection in connections:
    if connection[1] == 'Rome':
        routes_to_rome += 1
        total_flight_time +=200

print("Number of routes that lead to Rome:", routes_to_rome)
print("total flight time: ", total_flight_time)
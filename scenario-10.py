"""
    A city bus is a ring route bus which runs in circular fashion. That is,
    bus once starts at the source bus stop, halts at each bus stop in its route
    and at the end it reaches the source bus stop again.
    If there are n number of stops and if the bus starts at bus stop 1,
    then after nth bus stop, the next stop in the route will be bus stop number 1 always.
    If there are n stops, there will be n paths. One path connects two stops.
    Distances(in meters) for all paths in ring route is given in array path[] as given below:

    path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]

    Fare is determined based on the distance covered from source to destination stop
    as the distance between source and destination stops can be measured by looking at values
    in array path[] and fare can be calculated as per following criteria:

    If d =1000 metres, then fare=5 INR.

    (When calculating fare for other distances, if the calculated fare containing any fraction value,
    it should be ceiled.)
    For example, for distance 900 mtrs, when fare initially calculated is 4.5 which must be ceiled to 5.

    Path is in circular fashion and value at each index indicates distance till current stop
    from the previous one. Each index position can be mapped with values at same index in
    bus_stops[] array, which is a string array holding abbreviation of names for all stops as:

    “THANERAILWAYSTN” = ”TH”, “GAONDEVI” = “GA”, “ICEFACTROY” = “IC”, “HARINIWASCIRCLE” = “HA”,
    “TEENHATHNAKA” = “TE”, “LUISWADI” = “LU”, “NITINCOMPANYJUNCTION” = “NI”, “CADBURRYJUNCTION” = “CA”

    Given, n=8, where n is number of total bus stops.

    bus_stops = [“TH”, ”GA”, ”IC”, ”HA”, ”TE”, ”LU”, ”NI”, ”CA”]

    Write a code which take input as source and destination stops
    (in the format containing first two characters of the name of the bus stop)
    and calculate travel fare.

    Input Format
    Input the source stop.
    Input the destination stop.
    (Input should not be case sensitive)

    Constraints
    NA

    Output Format
    Output should be in the format:
    (float)x INR
    Any wrong input to the program should end up in displaying message:
    "INVALID INPUT"

    Sample Input 0
    NI
    HA

    Sample Output 0
    23.0 INR

    Sample Input 1
    CA
    CA

    Sample Output 1
    INVALID INPUT
"""

import math

path =      [800,  600,  750,  900,  1400, 1200, 1100, 1500]
bus_stops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"]

path = path + path
bus_stops = bus_stops + bus_stops

source = input().upper()
destinaton = input().upper()
distance = 0

if source in bus_stops and destinaton in bus_stops:

    for i in range(8):
        if source == bus_stops[i]:
            start = i
            for i in range(start,16):
                if destinaton == bus_stops[i]:
                    stop = i
                    break

    if start == stop:
        print("INVALID INPUT")
        exit()

    else:
        for i in range(start+1,stop+1):
            distance = distance + path[i]

    price = math.ceil((distance/200))
    print(f"{price:.1f} INR")

else:
    print("INVALID INPUT")
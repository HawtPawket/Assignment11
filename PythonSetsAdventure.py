# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor.
 # You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

# Example Code:

# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}



ourRoutes = {"LAX", "JFK", "CDG", "DXB", "ORD", "MDW", "ATL", "MBJ"}
competitorRoutes = {"JFK", "CDG", "LHR", "BKK", "KIN", "MDW", "DFW"}
print('''
Our Airlines routes''', ourRoutes)
print("Competitor Airlines routes", competitorRoutes)

commonRoutes = ourRoutes.intersection(competitorRoutes)
print('''
Destinations that both airlines fly to:''', commonRoutes)


ourUniqueRoutes = ourRoutes.difference(competitorRoutes)
print('''
Destinations unique to our airline:''', ourUniqueRoutes)


competitorUniqueRoutes = competitorRoutes.difference(ourRoutes)
print('''
Destinations unique to the competitor airline:''', competitorUniqueRoutes)


noCommonRoutes = ourRoutes.symmetric_difference(competitorRoutes)
print('''
Destinations that neither airline shares:''', noCommonRoutes)


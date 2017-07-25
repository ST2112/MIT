###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    copyCows = {}
    sortedVals = sorted(cows.values(), reverse=True)
    for val in sortedVals:
        for cow in cows:
            if cows[cow] == val and cow not in copyCows:
                copyCows[cow] = val
                
    shipments = []
    shippedNames = []
    
    while len(shippedNames) < len(copyCows): #until we have shipped all cows
        thisShipment = [] #start with an empty shipment
        remainingCap = limit  #empty shipment means full capacity (limit)
        
        
        for cow in copyCows: #dict values are descending, so march down
            if copyCows[cow] <= remainingCap and cow not in shippedNames: #we have a winner
                thisShipment.append(cow) #put the cow on the shipment
                remainingCap -= copyCows[cow] #deduct the weight from the capacity
                shippedNames.append(cow) #take the cow out of consideration
                    
        shipments.append(thisShipment) 
         
    return(shipments)
                    
                    
                


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    optimalPartition = []
    optimalNumShipments = len(cows) + 1 #we assume any acceptable partition will do no worse than one cow per shipment
    cowNames = cows.keys()
    #march through all possible partitions
    for thisPartition in (get_partitions(cowNames)):
        #start counting subsets (representing shipments) in this partition
        numShipments = 0
        reject_partition = False
        #examine each subset. Determine its weight, and if > capacity, 
        #break out of all inner loops and fetch another partition. 
        #Otherwise, increment the shipment count for later comparison to optimality.
        for shipment in thisPartition:
            #start count, start tare 
             numShipments += 1
             shipmentWeight = 0
             for cow in shipment:
                 shipmentWeight += cows[cow]
                 #break out of here if this attempted shipment exceeds capacity
                 if shipmentWeight > limit:
                     reject_partition = True
                     break
             #no need to continue through this partition if we've rejected a shipment 
             #in the partition
             if reject_partition:
                 break
        #if we made it through the entire outer for-loop (considered all subsets in this partition)
        #without rejecting, then the partition is a candidate for the optimal one.  Therefore consider
        #the number of subsets in the partition.
        if not reject_partition and (numShipments < optimalNumShipments):
            optimalPartition = thisPartition
            optimalNumShipments = numShipments
    return optimalPartition

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))



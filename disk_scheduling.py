#AUTHOR: Michael Graves
#DATE: 11.19.2025
#Disk_Scheduling Calculator
disk_arr = [ 53, 231, 46, 219, 184, 59, 35, 119, 151, 225 ]

def fcfs():

    """
    Function for calculating total head movement by utilizing first come first serve method
    """
    total_head_movement = 0
    for i in range(len(disk_arr)):
        if(i != 0):
            total_head_movement += abs((disk_arr[i] - disk_arr[i-1]))
    return total_head_movement

def scan():

    """
    Function for calculating total head movement by utilizing SCAN method
    """
    total_head_movement = 0
    decrease_queue = []
    increase_queue = []
    consolidated_queue = []

    #Sort arr to arrange queue to have decreasing values
    #Earlier values shall be closest to head value
    #Loop through remaining to construct higher value range
    for i in range(len(disk_arr)):
        if(disk_arr[i] < disk_arr[0]):
            decrease_queue.append(disk_arr[i])
    decrease_queue.sort(reverse=True)

    #Construct array of increasing values
    for j in range(len(disk_arr)):
        if(disk_arr[j] > disk_arr[0]):
            increase_queue.append(disk_arr[j])
        #Construct array of higher values
    increase_queue.sort()
    
    #Consolidate decrease_queue and increase_queue
    consolidated_queue.append(disk_arr[0])
    consolidated_queue.extend(decrease_queue)
    consolidated_queue.extend(increase_queue)

    #Sum consolidated queue
    for k in range(len(consolidated_queue)):
        if(k != 0):
            total_head_movement += abs((consolidated_queue[k] - consolidated_queue[k-1]))
    return total_head_movement

print("First Come First Serve Method: ")
print(fcfs())
print("SCAN method: ")
print(scan())

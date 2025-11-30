disk_arr = [99, 149, 189, 187, 159, 244, 23, 70, 34, 93]

def CSCAN():
    total_head_movement = 0
    increaseQueue = []
    wrapAroundQueue = []
    consolidated_queue = []

    for j in range(len(disk_arr)):
        if(disk_arr[j] > disk_arr[0]):
            increaseQueue.append(disk_arr[j])
        #Construct array of higher values
    increaseQueue.sort()

    for j in range(len(disk_arr)):
        if(disk_arr[j] < disk_arr[0]):
            wrapAroundQueue.append(disk_arr[j])
        #Construct array of higher values
    wrapAroundQueue.sort()

    #Consolidate decrease_queue and increase_queue
    consolidated_queue.append(disk_arr[0])
    consolidated_queue.extend(increaseQueue)
    consolidated_queue.extend(wrapAroundQueue)
    
    #Sum consolidated queue
    for k in range(len(consolidated_queue)):
        if(k != 0):
            total_head_movement += abs((consolidated_queue[k] - consolidated_queue[k-1]))
    return total_head_movement

print("Total head movement for CSCAN Method: ")
print(CSCAN())

import sys
import numpy as np

class BankerAlg:                                    # Class for the required variables and matrix for the banker's algorithm
    def __init__(self, numProc, numRecType, availMatrix, allocMatrix, requestMatrix):
        self.numProc = int(numProc)
        self.numRec = int(numRecType)
        self.available = np.array([int(i) for i in availMatrix])
        self.max = [[0 for i in range(self.numRec)]for j in range(self.numProc)]
        self.allocation = np.array([list(map(int, i)) for i in allocMatrix])
        self.need = [[0 for i in range(self.numRec)]for j in range(self.numProc)]
        self.request = np.array([list(map(int, i)) for i in requestMatrix])

# Function used to read a given File
def readFile(filename):
    with open(filename, "r") as f:
        numProcesses = int(f.readline())            # Receive the number of processes (first line)
        numResources = int(f.readline())            # Receive the number of resource types (second line)
        availableInst = f.readline().strip().split()# Split the starting number of resources

        matrix = []                                 # Initialize an empty array for processes

        for line in f.readlines():                  # Loop through each line
            lineSplit = line.strip().split()        # Strip and split each line for whitespaces
            matrix.append(lineSplit)                # Append the line to the matrix array

    return numProcesses, numResources, availableInst, matrix    # Return each element that will be used for the banker's algorithm

def calculateAvailable(data : BankerAlg):           # Function to calculate the available by adding each process that can have its request met
    status = [False for i in range(data.numProc)]   # Creating an array with a the size of the number of processes and setting them all to false
    check = np.less_equal(data.request, data.available) # Using NumPy less_equal to check whether each element in request is less than or equal to their corresponding element in available
    counter = 0                                     # counter to check elements a number of times in a while loop
    temp = 0                                        # temp variable to hold the result from freeing up a process and adding it to available
    while(counter != data.numProc):                 # while loop to check all processes multiple times in the case that the program needs to restart from the beginning
        check = np.less_equal(data.request, data.available) # Recheck the new available array to each element in the request matrix
        print()
        print("Testing:")
        for i in range(data.numProc):               # For loop to check each process
            test = np.less_equal(data.request[i], data.available) # Testing Particular elements to available
            if(status[i] == True):                  # If check to see if that element has passed / been freed. If so skip
                print("Process:",i,"SKIPPED")
                continue
            if(all(test)):                      # If check to see if each element in the matrix of request can be met.
                print("Process :",i , "Finished")
                print("Freeing up:",data.allocation[i])
                temp = np.add(data.available, data.allocation[i])   # add the elements of the matrix of allocation at i to the array of available and set it to temp
                data.available = temp               # Set the availble to the new temp
                status[i] = True                    # set the status of that process to true (freed)
                print("Available is now: ", data.available) # print the new available
            else:                                   # Othersise, when process at element i has neither been skipped or freed say that it has failed and loop again
                print(i,": Failed")
        counter += 1                                # Increment the counter outside the for loop in order to keep track of while loop iterations
        check = np.less_equal(data.request, data.available) # Recheck the new available array to each element in the request matrix


    # Determine whether or not the algorithm was safe or not
    if(not all(status)):                            # once the available has been calculated check if any status of a process still remains false (process was not freed)
        print()
        print("Not Safe")
        print("Processes (Starts at 0): ")
        for i in range(data.numProc):               # check which process was not freed and print that process number
            if(not all(check[i])):
                print(i)
            else:
                continue
        print("Are in involved in a Deadlock")
        print()
    else:                                           # Otheriwise, if the status of each element has been freed (true) print that the program is in a safe state
        print()
        print("All Programs have finished; Program is safe")
        print()

def main():
    while(True):                                    # While loop to constantly ask for another file from the user
        file = input("Please enter a file to test (Ctrl + C to exit): ")       # Asks the user for a file and assigns the name to variable calle file
        try:                                                # Determines whether or not the given file exists
            numProc, numRec, availInst, matrix = readFile(file) # Set each variable to the corresponding return values of reading the file
            allocationMatrix = matrix[:numProc]             # Set the first half of the returned matrix to a matrix called allocationMatrix
            requestMatrix = matrix[numProc:]                # set the second half of the returned matrix to a matrix called requestMatrix
            
            bankerAlg = BankerAlg(numProc, numRec, availInst, allocationMatrix, requestMatrix) # Create a variable of type BankerAlg called bankerAlg with the variables above
            print("Starting Instance:", bankerAlg.available)# Print starting available
            calculateAvailable(bankerAlg)                   # Calculate the remaining available of the rest of the processes
        except IOError as err:                              # Prints error when the file is determined not to exist
            print("File does not exist. Try Again")
            print()

    # if(argc != 2):                                  # Check whether or not the program has been given the correct number of arguments
    #     print("usage : main <input file>")
    #     return -1
    
    # numProc, numRec, availInst, matrix = readFile(sys.argv[1]) # Set each variable to the corresponding return values of reading the file
    # allocationMatrix = matrix[:numProc]             # Set the first half of the returned matrix to a matrix called allocationMatrix
    # requestMatrix = matrix[numProc:]                # set the second half of the returned matrix to a matrix called requestMatrix
    
    # bankerAlg = BankerAlg(numProc, numRec, availInst, allocationMatrix, requestMatrix) # Create a variable of type BankerAlg called bankerAlg with the variables above
    # print("Starting Instance:", bankerAlg.available)# Print starting available
    # calculateAvailable(bankerAlg)                   # Calculate the remaining available of the rest of the processes
    # #safetyAlgorithm(bankerAlg)


if __name__ == '__main__':
    main()
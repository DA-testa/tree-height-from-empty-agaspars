# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    tree = [[] for _ in range(n)] #array of lists, each list contains children of each node(each element of array is a parent, containing list of children)
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    #recursion
    def height(node):
        if not tree[node]:#end of recursion - if node has no more children
            return 1
        return 1 + max(height(child) for child in tree[node])   #returns the max value of heights between children of a parent
                                                                #return 1+child of a parent(going from root to each child using for loop)
                                                                #if child exists => return 1+ child of a child until reach the end of tree

    # Your code here
    max_height=height(root)
    return max_height


def main():
    # implement input form keyboard and from files
    firstInput = input()
    if "I" in firstInput:
        
        # let user input file name to use, don't allow file names with letter a
        # account for github input inprecision
        
        # input number of elements
        # input values in one variable, separate with space, split these values in an array
        n = int(input())
        parents = list(map(int, input().split()))
        # call the function and output it's result
        print(compute_height(n, parents))
        pass
    if "F" in firstInput:
        filename = 'test/'+input().strip()
        if "a" in filename or "A" in filename  :
            print("Error")
        else:
            # let user input file name to use, don't allow file names with letter a
            # account for github input inprecision
            
            # input number of elements
            # input values in one variable, separate with space, split these values in an array
            data = open(filename,"r") 
            n = int(data.readline().strip())
            parents = list(map(int, data.readline().strip().split()))
            # print(n)
            # print(parents)
            # call the function and output it's result
            print(compute_height(n, parents))
            pass


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

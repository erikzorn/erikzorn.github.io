def solution(A, E):
    # write your code in Python 2.7
    longest_path = 0
    # start at the last index (last node) and DFS for continuous path
    last_index = len(A) - 1
    i = last_index
    # outer while allows program to DFS from every node
    while ( i >= 0 ):
        last_value = A[i]
        # next_value = A[i / 2]
        current_path = 0
        marked_indices = [i]
        stack = [i] # initialze stack with first index
        current_index = i
        # try until every DFS path has been attempted from that node
        while (len(stack) > 0):
            
            # update longest path
            if len(stack) - 1 > longest_path:
                longest_path = len(stack)
                
            # try to go down left in tree
            if ( current_index*2 < len(A) and A[current_index*2] == last_value 
            and current_index*2 not in marked_indices):
                next_value = A[current_index*2]
                marked_indices.append(current_index*2)  # mark index visited
                stack.append(current_index*2)
                
            # try to go down rihgt
            elif ( current_index*2+1 < len(A) and A[current_index*2+1] == last_value 
            and current_index*2 + 1 not in marked_indices):
                next_value = A[current_index*2 + 1]
                marked_indices.append(current_index*2 + 1)  # mark index visited
                stack.append(current_index*2 + 1)
                
            # try to go to parent  
            elif (A[current_index/2] == last_value and current_index/2 not in marked_indices):
                next_value = A[current_index / 2]
                marked_indices.append(current_index / 2)    # mark index visited
                stack.append(current_index*2 + 1)
                
            # else move back a vertex and continue DFS
            else:
                stack.pop()
            print(stack)
        i -= 1  # decrement to start from next index
                
    return longest_path

A = [1,1,2,4,5,7,9]
E = []
print(solution(A, E))
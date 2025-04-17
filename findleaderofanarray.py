def find_leaders(arr):  
  n = len(arr)  
  leaders = []  

  # Traverse the array from left to right  
  for i in range(n - 1):  
      is_leader = True  # Assume arr[i] is a leader initially  

      # Compare arr[i] with elements to its right  
      for j in range(i + 1, n):  
          if arr[i] < arr[j]:  
              is_leader = False  # arr[i] is not a leader  
              break  # No need to check further  

      # If is_leader is still True, arr[i] is a leader  
      if is_leader:  
          leaders.append(arr[i])  

  # The rightmost element is always a leader  
  leaders.append(arr[n - 1])  

  return leaders  

# Example usage:  
arr = [3938, 93939, 999999, 49483,5969,686]  
result = find_leaders(arr)  
print("Leaders in the array:", result)  
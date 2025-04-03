def checksorted(a):
    Length = len(a)
    if Length == 0 or Length == 1:
        return True
    return a[0] <= a[1] and checksorted(a[1:])

a = [1,2,3,4,5,6,7]

if checksorted(a):
    print("\n Yes your list is sorted!")
else:
    print("\n No your list is not sorted!")
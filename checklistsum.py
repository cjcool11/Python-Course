def checkarraysum(a):
    Length = len(a)
    if Length == 1:
        return a[0]
    return a[0] + checkarraysum(a[1:])

a = [1,7,5]

print("Your List's sum is: ",checkarraysum(a))
dictionary = {'rap': 1}
def function(lst):
    s = []
    for x in lst:
        s.append(x)
    return s
    
ans = function([dictionary])[0]
print(ans)
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lyeni = []

def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)

        else:
            lyeni.append(i)

flatten(l)
print(lyeni)
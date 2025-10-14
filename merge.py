def Sort(Array: list) -> None:

    for i in range(0, len(Array)): 

        for k in range(1, len(Array) - i):

            if Array[k] < Array[k - 1]:
                Temp = Array[k]
                Array[k] = Array[k - 1]
                Array[k - 1] = Temp

def merge_list(a: list, b: list) -> list: 

    if not isinstance(a, list) and not isinstance(b, list):
        raise TypeError
    
    c = a + b
    Sort(c)
    return c
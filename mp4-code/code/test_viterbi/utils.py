from csv import reader
smoothing_constant = 1e-10
def read_files():
    test = []
    with open('test.txt','r') as f:
        l = f.read()
        test.append(l.split())
    
    with open('output.txt','r') as f:
        output = f.read()

    emission = []
    with open('emission.txt','r') as f:
        c = reader(f)
        for line in c:
            emission.append([line[0],line[1],float(line[2])])
    
    transition = []
    with open('transition.txt','r') as f:
        c = reader(f)
        for line in c:
            transition.append([line[0],line[1],float(line[2])])

    return test, emission, transition, output

def get_nested_dictionaries(emission, transition):
    """
    Output:
    em dict(dict(float)): Outer dictionary keys are tags, inner dictionary keys are words. Values are probabilities. 
    tr dict(dict(float)): Outer dictionary keys are preceding tags, inner dictionary keys are succeeding tags. Values are probabilities. 
    """    
    tr, em = {}, {}

    for w, t, p in emission:
        if not t in em:
            em[t] = {}
        em[t][w] = p + smoothing_constant #THIS SMOOTHING IS NOT CORRECT AND IS ONLY USED FOR THE DUMMY EXAMPLE!

    for t1, t2, p in transition:
        if not t1 in tr:
            tr[t1] = {}
        tr[t1][t2] = p + smoothing_constant #THIS SMOOTHING IS NOT CORRECT AND IS ONLY USED FOR THE DUMMY EXAMPLE!
    return em, tr
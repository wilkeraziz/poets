from collections import defaultdict

def rdefaultdict(levels, cls):
    """Recursively constructs a defaultdict with N levels of dictionaries ending in a given type"""
    if levels < 1: 
        raise ValueError, 'At least 1 level is necessary'
    obj = defaultdict(cls)
    cls = lambda : obj
    if levels == 1:
        return cls()
    return rdefaultdict(levels - 1, cls)

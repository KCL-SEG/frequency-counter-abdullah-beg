"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        item = str(item)
        if item in frequencies.keys():
            frequencies[item] = frequencies[item] + 1
        else:
            print(f'{item}')
            frequencies.update({item : 1})

    return frequencies

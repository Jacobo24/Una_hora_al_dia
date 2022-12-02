def alphabet_war(fight):
    d = 0
    i = 0
    left = {'w': 4, 'p': 3, 'b': 2, 's':1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z':1}
    for letter  in fight: 
        if letter in left:
            i += left[letter]
        elif letter in right:
            d += right[letter]  
    if i > d:
        return 'Left side wins!'
    elif d > i:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
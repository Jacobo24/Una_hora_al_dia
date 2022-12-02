def rgb(r, g, b):
    return ''.join([hex(min(max(x, 0), 255))[2:].zfill(2) for x in [r, g, b]]).upper()
    pass
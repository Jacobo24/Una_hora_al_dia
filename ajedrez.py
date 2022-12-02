def knight_vs_king (knight_position, king_position):
    pos = "ABCDEFGH"
    a = pos.index(knight_position[1])
    b = pos.index(king_position[1])
    if abs(knight_position[0] - king_position[0]) == 2 and abs(a - b) == 1:
        return "Knight"
    elif abs(knight_position[0] - king_position[0]) == 1 and abs(a - b) == 2:
        return "Knight"
    elif abs(knight_position[0] - king_position[0]) == 1 and abs(a - b) == 0:
        return "King"
    elif abs(knight_position[0] - king_position[0]) == 0 and abs(a - b) == 1:
        return "King"
    elif abs(knight_position[0] - king_position[0]) == 1 and abs(a - b) == 1:
        return "King"
    else:
        return "None"
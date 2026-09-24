def checkmate(board):
    board = board.strip().split("\n")

    size = len(board)

    # ตรวจสอบว่า board เป็นสี่เหลี่ยม
    for row in board:
        if len(row) != size:
            return

    # หา King
    king_row = -1
    king_col = -1

    for r in range(size):
        for c in range(size):
            if board[r][c] == "K":
                king_row = r
                king_col = c

    # ไม่มี King
    if king_row == -1:
        return

    # -------------------------
    # Pawn
    # -------------------------
    # Pawn โจมตีจากด้านบนลงล่าง
    for dc in [-1, 1]:
        r = king_row - 1
        c = king_col + dc

        if 0 <= r < size and 0 <= c < size:
            if board[r][c] == "P":
                print("Success")
                return

    # -------------------------
    # Bishop / Queen
    # -------------------------
    directions_diagonal = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions_diagonal:
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]

            if piece != ".":
                if piece == "B" or piece == "Q":
                    print("Success")
                    return
                break

            r += dr
            c += dc

    # -------------------------
    # Rook / Queen
    # -------------------------
    directions_straight = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions_straight:
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]

            if piece != ".":
                if piece == "R" or piece == "Q":
                    print("Success")
                    return
                break

            r += dr
            c += dc

    print("Fail")

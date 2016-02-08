def cover(board, lab=1, top=0, left=0, side=None):
    if side is None: side = len(board)
    #side lenth of subboard
    s=side//2
    # Offsets for outer/inner squares of subboards:
    offsets = (0, -1), (side-1, 0)
    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            #if outer coner is not set...
            if not board[top+dy_outer][left+dx_outer]:
                #label the inner coner
                board[top+s+dy_inner][left+dx_inner] =lab
    #next label
    lab +=1
    if s>1:
        for dy in[0,s]:
            for dx in [0,s]:
                #recursive calls if s is atleast 2
                lab = cover(board, lab, top+dy, left+dx, s)

    #return the next available label
    return lab

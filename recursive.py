def ins_sort_rec(seq, i):
    if i==0: return    # Base case -- do nothing
    ins_sort_rec(seq, i-1)    # Sort 0..i-1
    j = i   # Start "walking" down
    while j > 0 and seq[j-1] > seq[j]: # Look for OK spot
        seq[j-1], seq[j] = seq[j], seq[j-1] # Keep moving seq[j] down
        j -= 1  # Decrement j

def bouncing_balls(h, bounce, window):
    if h <= 0 or bounce >= 1 or bounce <= 0 or window >= h: return -1
    count = 0
    while window < h:
        count += 1
        h = h * 0.66
        if window<h: count += 1
    return count
    

test1 = print(bouncing_balls(2, 0.5, 1))
test2 = print(bouncing_balls(3, 0.66, 1.5))

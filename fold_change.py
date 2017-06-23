def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    return ((1 + ((RK * (1+c/KdA)**2) / ((1+c/KdA)**2 + Kswitch*(1+c/KdI)**2)))**-1)

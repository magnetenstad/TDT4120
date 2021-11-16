
# FORD-FULKERSON-METHOD(G, s, t)
# 1 initialize flow f to 0
# 2 while there exists an augmenting path p in the residual network Gf
# 3     augment flow f along p
# 4 return f

# FORD-FULKERSON(G, s, t)
# 1 for each edge (u, v) in G.E
# 2     (u, v).f = 0
# 3 while there exists a path p from s to t in the residual network Gf
# 4     cf(p) = min{cf(u, v) : (u, v) is in p}
# 5     for each edge (u, v) in p
# 6         if (u, v) in E
# 7             (u, v).f = (u, v).f + cf(p)
# 8         else (u, v).f = (u, v).f - cf(p)

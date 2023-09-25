# Calculate reactions due to uniformly distribuited load
from numpy import ndarray

def exec(n: int, distribuited_loads: ndarray, A: int, B:int):      
    xStart = distribuited_loads[n,0]
    xEnd = distribuited_loads[n,1]
    fy = distribuited_loads[n,2]
    
    fy_Res = fy*(xEnd-xStart)
    x_Res = xStart + 0.5*(xEnd-xStart)

    la_p = A-x_Res
    mp = fy_Res*la_p
    la_vb = B-A
 
    Vb = mp/la_vb
    Va = -fy_Res-Vb
    
    return Va, Vb
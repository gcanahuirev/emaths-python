# Calculate reactions due to point moments
from numpy import ndarray


def exec(n:int, point_moments: ndarray, A:int, B:int):
    xm = point_moments[n,0]
    m = point_moments[n,1]
    la_vb = B-A

    Vb = m/la_vb
    Va = -Vb

    return Va, Vb
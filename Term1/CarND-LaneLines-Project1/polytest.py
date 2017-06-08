import numpy as np

xl = np.array([100,470])
yl = np.array([539,275])

bias = 5
left_bias = 0.71351351 * bias
right_bias = 0.61395349 * bias
left_lane_poly  = np.poly1d([ -0.71351351 , 610.35135135 + left_bias])
right_lane_poly  = np.poly1d([ 0.61395349 ,-13.55813953 + right_bias])



print (  (left_lane_poly -  431.97297385).roots[0] )


print (  (right_lane_poly -  539
          ).roots[0] )

counter = 0
str(counter)

counter += 1

print(counter)

import math
np.isnan

lanes = [0, 0, float('nan'), 719], [-52.650655021833963, 0, 1146.7292576419213, 719]
if  not isinstance(lanes, (list,tuple,set)):
    print("not list")
else:
    for lane in lanes:
        if np.isnan(np.min(lane)):
            print("nan found")
    print("list")

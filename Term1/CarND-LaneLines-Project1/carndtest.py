import numpy as np
from itertools import chain
lines = [[[498, 316, 853, 538]],
         [[497, 319, 787, 508]],
         [[698, 451, 832, 538]],
         [[496, 318, 650, 418]],
         [[310, 422, 355, 392]],
         [[435, 341, 449, 331]],
         [[319, 425, 363, 392]],
         [[437, 340, 448, 332]],
         [[527, 335, 853, 539]],
         [[406, 357, 415, 351]],
         [[528, 340, 545, 351]],
         [[636, 410, 831, 537]],
         [[317, 419, 356, 392]]]



def highest_lane_point(points):
    highest_point = min(points, key=lambda x: x[1])
    return highest_point

def get_slopes_and_points(lines):
    left_lane_points = []
    right_lane_points = []
    left_lane_slopes = []
    right_lane_slopes = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        line_slope = (y2 - y1) / (x2 - x1)
        if line_slope > 0:
            right_lane_slopes.append(line_slope)
            right_lane_points.append([x1, y1])
            right_lane_points.append([x2, y2])
        else:
            left_lane_slopes.append(line_slope)
            left_lane_points.append([x1, y1])
            left_lane_points.append([x2, y2])

    return left_lane_slopes, left_lane_points,right_lane_slopes,right_lane_points

def extrapolate_x_coord(point_on_line, slope, y_coord):
    bias = point_on_line[1] - slope * point_on_line[0]
    x_coord = (y_coord - bias) / slope
    return x_coord



def find_lane_line_coords(lines):

    left_lane_slopes, left_lane_points, right_lane_slopes, right_lane_points = get_slopes_and_points(lines)

    #average slope
    left_average_slope = np.average(left_lane_slopes)
    right_average_slope = np.average(right_lane_slopes)

    highest_right_lane_coord = highest_lane_point(right_lane_points)
    highest_left_lane_coord = highest_lane_point(left_lane_points)
    lowest_left_lane_coord = [ extrapolate_x_coord(highest_left_lane_coord,left_average_slope,539),539]
    lowest_right_lane_coord = [extrapolate_x_coord(highest_right_lane_coord, right_average_slope, 539), 539]
    left_lane = highest_left_lane_coord + lowest_left_lane_coord
    right_lane = highest_right_lane_coord + lowest_right_lane_coord
    lines = np.array([left_lane,right_lane],np.int32)
    return lines




print( find_lane_line_coords(lines))
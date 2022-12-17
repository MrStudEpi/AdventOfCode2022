#!/usr/bin/env python3

import re

f = open('files/final', 'r')

lines = []

for line in f:
    lines.append(line.strip())

def parse():
    reg = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): '
                         r'closest beacon is at x=(-?\d+), y=(-?\d+)')

    sensors = {}
    beacons = {}
    for line in lines:
        match = reg.match(line)
        if match:
            sx, sy = int(match.group(1)), int(match.group(2))
            bx, by = int(match.group(3)), int(match.group(4))
            sensors[sx, sy] = abs(sx -bx) + abs(sy - by)
            beacons[sx, sy] = bx, by
    return sensors, beacons

def exo1(parsed_data, row):
    not_there= set()
    beacon_x = set()
    sensor_distance, beacons = parsed_data
    for point, val in sensor_distance.items():
        sx, sy = point
        bx, by = beacons[sx, sy]
        if by == row:
            beacon_x.add(bx)
        if (window := val - abs(row- sy)) >= 0:
            not_there.update([x for x in range(sx-window, sx+window+1)])
    not_there.difference_update(beacon_x)
    return len(not_there)

def exo2(parsed_data, max_value):
    x_mult = 4_000_000
    sensor_distance, _ = parsed_data
    checked_points = set()
    for point, val in sensor_distance.items():
        sx, sy = point
        for side in range(4):
            for i in range(val+1):
                if side == 0:
                    cx = sx + val + 1 - i
                    cy = sy + i
                elif side == 1:
                    cx = sx - i
                    cy = sy + val + 1 - i
                elif side == 2:
                    cx = sx - val - 1 + i
                    cy = sy - i
                else:
                    cx = sx + i
                    cy = sy - val - 1 + i
                if (0 <= cx <= max_value and 0 <= cy <= max_value
                    and (cx, cy) not in checked_points):
                    found = all((abs(cx - otherx) + abs(cy - othery)) > other_distance 
                                for (otherx, othery), other_distance in sensor_distance.items())
                if found:
                    return x_mult * cx + cy
                else:
                    checked_points.add((cx, cy))
            
parsed_data = parse()
solution1 = exo1(parsed_data, 2_000_000)
print('Exo 1:', solution1)
solution2 = exo2(parsed_data, 4_000_000)
print('Exo 2:', solution2)
PATHS = [
    ['Tehran', 'Karaj'],
    ['Karaj', 'Qazvin'],
    ['Qazvin', 'Rasht'],
    ['Karaj', 'Chaloos'],
    ['Chaloos', 'Shahsavar'],
    ['Shahsavar', 'Ramsar'],
    ['Ramsar', 'Rasht'],
    ['Qazvin', 'Zanjan'],
    ['Zanjan', 'Manjil'],
    ['Manjil', 'Rasht'],
]

paths = []
for p in PATHS:
    paths.append(p)
    paths.append([p[1], p[0]])

ORIGIN = 'Rasht'
DESTINATION = 'Tehran'

def find_next_point(origin, history: list = None):
    if history is None:
        next_points = [p[1] for p in paths if p[0] == origin]
    else:
        next_points = [p[1] for p in paths if p[0] == origin and p[1] not in history]

    if len(next_points) == 0:
        return None
    # پس اینجا مطمئن هستیم که نقاط بعدی وجود دارند

    ways = [] # مجموعه راه هایی که با origin شروع میشوند
    for point in next_points:
        # point: B
        if point == DESTINATION:
            ways.append([DESTINATION])
        else:
            if history is None:
                k = find_next_point(point, [origin]) 
            else:
                k = find_next_point(point, history + [origin]) 
            if k is not None:
                ways.extend(k)
    
    for way in ways:
        # way: [B]
        way.insert(0, origin)
        # way: [A, B]
    # ways: [[A, B]]
    return ways

result = find_next_point(ORIGIN)
print(result)



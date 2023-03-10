def closest(points, target_point):
    def distance(point):
        x, y = point
        dx = x - tx
        dy = y - ty
        return dx**2 + dy**2

    tx, ty = target_point
    return min(points, key=distance)

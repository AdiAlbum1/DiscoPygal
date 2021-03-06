from bindings import CGALPY

Ker = CGALPY.Ker
Pol2 = CGALPY.Pol2
import math

Gmpq, FT = Ker.Gmpq, Ker.FT
Point_2 = Ker.Point_2
Segment_2 = Ker.Segment_2
Vector_2 = Ker.Vector_2
Aff_transformation_2 = Ker.Aff_transformation_2
Rotation = Ker.Rotation
Polygon_2 = Pol2.Polygon_2


def point_2_to_xy(p):
    return p.x().to_double(), p.y().to_double()


def xy_to_point_2(x, y):
    return Point_2(x, y)


def coords_list_to_polygon_2(lst):
    lst0 = []
    for i in range(len(lst) // 2):
        lst0.append(Point_2(lst[2 * i], lst[2 * i + 1]))
    p = Polygon_2(lst0)
    if p.is_clockwise_oriented(): p.reverse_orientation()
    return p


def tuples_list_to_polygon_2(lst):
    lst0 = []
    for tuple in lst:
        lst0.append(Point_2(tuple[0], tuple[1]))
    p = Polygon_2(lst0)
    if p.is_clockwise_oriented(): p.reverse_orientation()
    return p


def polygon_2_to_tuples_list(polygon):
    lst = [(p.x().to_double(), p.y().to_double()) for p in polygon.vertices()]
    return lst


def path_point_to_xyzd(p):
    x = p[0].to_double()
    y = p[1].to_double()
    z = p[2].to_double()
    d = p[3]
    return (x, y, z, d)

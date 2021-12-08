#!/usr/bin/env python3

import argparse
import sys

class Point:
    _x: int
    _y: int
    """
    Represents a point on a line segment.
    """
    def __init__(self, x: int, y: int):
        """
        A point referenced by a coordinate in the x/y plane.

        Arguments:
            x (int): The distance of the point along the x axis.
            y (int): The distance of the point along the x axis.
        """
        self._x = x
        self._y = y

    def __eq__(self, other) -> bool:
        """
        Whether self and other are equal points.

        Return (bool): True if self and other are the same point, False
        otherwise.

        >>> a = Point(1, 2)
        >>> b = Point(1, 2)
        >>> c = Point(3, 4)
        >>> a == b
        True
        >>> b == c
        False
        """
        return self._x == other._x and self._y == other._y

    def __ne__(self, other) -> bool:
        """
        Whether self and other are not equal points.

        Return (bool): True if self and other are not the same point, False
        otherwise.

        >>> a = Point(1, 2)
        >>> b = Point(1, 2)
        >>> c = Point(3, 4)
        >>> a != b
        False
        >>> b != c
        True
        """
        return not self == other
    
    def __hash__(self) -> int:
        """
        Return a hash of the point so it can be used in sets.

        >>> p1 = Point(1, 2)
        >>> p2 = Point(3, 0)
        >>> s = set()
        >>> s.add(p1)
        >>> len(s)
        1
        >>> s.add(p2)
        >>> len(s)
        2
        >>> s.add(p2)
        >>> len(s)
        2
        """
        return hash(self._x) + hash(self._y)

    def __str__(self) -> str:
        """
        >>> print(Point(3, 9))
        (3, 9)
        """
        return f'({self._x}, {self._y})'

    def __repr__(self):
        """
        >>> Point(3, 9)
        Point(x=3, y=9)
        """
        return f'Point(x={self._x}, y={self._y})'
    
    def get_x(self) -> int:
        """
        A getter for the x value of the point's coordinate.

        Return (int): The x value of the cooridinate.

        >>> Point(1, 2).get_x()
        1
        """
        return self._x

    def get_y(self) -> int:
        """
        A getter for the x value of the point's coordinate.

        Return (int): The y value of the cooridinate.

        >>> Point(1, 2).get_y()
        2
        """
        return self._y

class Slope:
    """
    The slope between two Points.

    This assumes that points are either horizontal, vertical, or that the rise
    and run of the slope are equal.
    """
    _rise: int
    _run: int
    def __init__(self, point1: Point, point2: Point):
        """
        Construct the slope from two points.

        Raise:
            ValueError if the slope is not vertical, horizontal, or diagonal
            with a slope of 1 or -1.
        """
        self._rise = Slope._get_rise_or_run_value(point1.get_y(), point2.get_y())
        self._run = Slope._get_rise_or_run_value(point1.get_x(), point2.get_x())

        if not self.is_horizontal_or_vertical():
            delta_y = abs(point2.get_y() - point1.get_y())
            delta_x = abs(point2.get_x() - point1.get_x())
            if delta_y != delta_x:
                raise ValueError("A diagonal slope must be 1 or -1.")

    def get_rise(self) -> int:
        """
        Get the incremental rise from the Slope.

        Return (int): The x delta of the slope.

        >>> s = Slope(Point(0, 9), Point(5, 9))
        >>> s.get_rise()
        0
        """
        return self._rise

    def get_run(self) -> int:
        """
        Get the incremental run from the Slope.

        Return (int): The y delta of the slope.

        >>> s = Slope(Point(0, 9), Point(5, 9))
        >>> s.get_run()
        1
        """
        return self._run

    def is_horizontal_or_vertical(self):
        """
        Return whether the slope is horizontal or vertical.

        Return (bool): True if the points are vertical or horizontal from each
        other, false otherwise.

        >>> Slope(Point(0, 9), Point(2, 9)).is_horizontal_or_vertical()
        True
        >>> Slope(Point(7, 0), Point(7, 4)).is_horizontal_or_vertical()
        True
        >>> Slope(Point(0, 0), Point(8, 8)).is_horizontal_or_vertical()
        False

        """
        return self.get_rise() == 0 or self.get_run() == 0

    @staticmethod
    def _get_rise_or_run_value(value1, value2):
        """
        Assume values increase by one or not at all.

        >>> Slope._get_rise_or_run_value(1, 1)
        0
        >>> Slope._get_rise_or_run_value(1, 0)
        -1
        >>> Slope._get_rise_or_run_value(0, 30)
        1
        """
        if value1 == value2:
            return 0
        elif value2 < value1:
            return -1
        else:
            return 1

class Segment:
    _point1: Point
    _point2: Point
    _slope: Slope

    """
    A line segment defined by two Points.
    """
    def __init__(self, point1, point2):
        """
        Initialize the line segment by two end points.

        Arguments:
            point1 (Point): An endpoint on Segment.
            point2 (Point): An endpoint on Segment.
        """
        self._point1 = point1
        self._point2 = point2
        self._slope = Slope(self._point1, self._point2)

    def __str__(self):
        """
        >>> print(Segment(Point(6, 4), Point(2, 0)))
        (6, 4) -> (2, 0)
        """
        return f'{self._point1} -> {self._point2}'

    def __repr__(self):
        """
        >>> Segment(Point(6, 4), Point(2, 0))
        Segment(Point(x=6, y=4), Point(x=2, y=0))
        """
        return (f'Segment(Point(x={self._point1.get_x()}, y={self._point1.get_y()}), '
                f'Point(x={self._point2.get_x()}, y={self._point2.get_y()}))')

    def is_horizontal_or_vertical(self) -> bool:
        """
        Return whether the slope is horizontal or vertical.

        Return (bool): True if the slope is vertical or horizontal, false
        otherwise.

        >>> Segment(Point(0, 9), Point(2, 9)).is_horizontal_or_vertical()
        True
        >>> Segment(Point(7, 0), Point(7, 4)).is_horizontal_or_vertical()
        True
        >>> Segment(Point(0, 0), Point(8, 8)).is_horizontal_or_vertical()
        False
        """
        return self._slope.is_horizontal_or_vertical()

    def get_points(self) -> list[Point]:
        """
        Return the set of points on the line segment, including the end points.

        Returns

        >>> s = Segment(Point(0, 9), Point(2, 9))
        >>> s.get_points()
        [Point(x=0, y=9), Point(x=1, y=9), Point(x=2, y=9)]
        """
        points = [self._point1]
        point = self._point1
        while point != self._point2:
            new_x = point.get_x() + self._slope.get_run()
            new_y = point.get_y() + self._slope.get_rise()
            point = Point(new_x, new_y)
            points.append(point)
        return points

    def get_intersection(self, other):
        """
        Return the set of points for which self intersects with other.

        >>> s1 = Segment(Point(0, 9), Point(5, 9))
        >>> s2 = Segment(Point(0, 9), Point(2, 9))
        >>> s1.get_intersection(s2)
        [Point(x=0, y=9), Point(x=1, y=9), Point(x=2, y=9)]
        >>> s2.get_intersection(s1)
        [Point(x=0, y=9), Point(x=1, y=9), Point(x=2, y=9)]
        """
        return [a for a in self.get_points() if a in other.get_points()]

def get_point(coordinate_str):
    """
    Given the coordinate string, return the Point that represents it.

    >>> get_point('9,4')
    Point(x=9, y=4)
    """
    x, y = coordinate_str.strip().split(',')
    return Point(int(x), int(y))

def get_segment(line):
    """
    Given a segment description, return the Segment object that represents it.
    >>> print(get_segment('9,4 -> 3,4'))
    (9, 4) -> (3, 4)
    """
    point1, _, point2 = line.strip().split()
    point1 = get_point(point1)
    point2 = get_point(point2)
    return Segment(point1, point2)

def parse_args():
    parser = argparse.ArgumentParser(
            description='Find the intersection of lines.')
    parser.add_argument(
            'segments_file',
            type=argparse.FileType('rt'),
            default=sys.stdin,
            help='A file with a set of segment descriptions.')
    parser.add_argument(
            '-d', '--count_diagonal',
            action="store_true",
            default=False,
            help='Count diagonal intersections as well.')
    return parser.parse_args()

def main():
    args = parse_args()

    seen_points = set()
    intersecting_points = set()
    for line in args.segments_file:
        s = get_segment(line)
        if not args.count_diagonal and not s.is_horizontal_or_vertical():
            continue
        points = s.get_points()
        for point in points:
            if point in seen_points:
                intersecting_points.add(point)
        seen_points.update(set(points))

    print(len(intersecting_points))
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())

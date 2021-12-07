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

        Return (bool): True if self and other are the same point, false
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
    and run of the slope is equal.
    """
    _rise: int
    _run: int
    def __init__(self, point1: Point, point2: Point):
        """
        Construct the slope from two points.
        """
        self._rise = Slope._get_rise_or_run_value(point1.get_y(), point2.get_y())
        self._run = Slope._get_rise_or_run_value(point1.get_x(), point2.get_x())

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
        return self._slope.get_rise() == 0 or self._slope.get_run() == 0

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
    return parser.parse_args()

def main():
    args = parse_args()

    segments = []
    for line in args.segments_file:
        s = get_segment(line)
        if not s.is_horizontal_or_vertical():
            continue
        segments.append(get_segment(line))

    intersecting_points = []
    for i, s1 in enumerate(segments):
        for s2 in segments[i+1:]:
            new_points = s1.get_intersection(s2)
            for new_point in new_points:
                if new_point in intersecting_points:
                    continue
                intersecting_points.append(new_point)
    print(len(intersecting_points))
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())

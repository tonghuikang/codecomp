# Geometry

General advice

- Geometry problems are prone to rounding errors
  - Avoid taking square root if possible.
  - Avoid converting into floats if possible.
  - You may need to allowance for rounding.



To determine whether three points lie on the same line 

-  calculate the area of the triangle defined by the three points

```python
0.5*(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
```



To check whether a candidate point is inside a triangle defined by three points

- Calculate the area of the triangle
- Calculate the area of the point with two points of the triangle

https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/



Order the points such that a shape is not deformed

- I haven't seen this question yet
- 
- Use 2-Opt from TSP?



Calculate the area of a polygon defined by a sequence of points

- 



To obtain the circle defined by three points

- assuming the points
  - are not collinear

https://stackoverflow.com/questions/28910718/give-3-points-and-a-plot-circle



To obtain the circle defined by two points and a radius

- assuming the points 
  - are not more than two times the specified radius
  - are not the same point

https://rosettacode.org/wiki/Circles_of_given_radius_through_two_points#Python


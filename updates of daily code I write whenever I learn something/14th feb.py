# cook your dish here
'''RECTSQ''' """important"""
import math

for t in range(int(input())):
    l, b = map(int, input().split())
    s = math.gcd(l, b)
    # Calculate how many squares of side s fit along l and b
    num_squares_along_l = l // s
    num_squares_along_b = b // s
    total_squares = num_squares_along_l * num_squares_along_b

    print(total_squares)

"""read about all math function from google"""
"""
## Summary:

### Data Analysis Key Findings

The exploration of Python's `math` module revealed a comprehensive set of functions and constants crucial for various numerical and scientific computations. Key findings include:

*   **Constants:**
    *   `math.pi`: Represents the mathematical constant $\pi$ (approximately 3.141592653589793).
    *   `math.e`: Represents the mathematical constant e (approximately 2.718281828459045).
    *   `math.tau`: Represents the mathematical constant $\tau = 2\pi$ (approximately 6.283185307179586).
    *   `math.inf`: Represents positive infinity.
    *   `math.nan`: Represents "Not a Number".
*   **Arithmetic Functions:**
    *   `math.ceil(x)`: Returns the smallest integer greater than or equal to $x$.
    *   `math.floor(x)`: Returns the largest integer less than or equal to $x$.
    *   `math.fabs(x)`: Returns the absolute value of $x$.
    *   'math.lcm(integers): return least common multiple. 
    *   `math.gcd(a, b)`: Returns the greatest common divisor of $a$ and $b$.
    *   `math.perm(n, k)`: Returns the number of ways to choose $k$ items from $n$ items without repetition and with order (permutations).
    *   `math.comb(n, k)`: Returns the number of ways to choose $k$ items from $n$ items without repetition and without order (combinations).
*   **Power and Logarithmic Functions:**
    *   `math.pow(x, y)`: Returns $x$ raised to the power $y$.
    *   `math.sqrt(x)`: Returns the square root of $x$.
    *   `math.exp(x)`: Returns $e$ raised to the power $x$.
    *   `math.log(x, base)`: Returns the logarithm of $x$ to the given base. If no base is provided, it defaults to the natural logarithm (base e).
    *   `math.log2(x)`: Returns the base-2 logarithm of $x$.
    *   `math.log10(x)`: Returns the base-10 logarithm of $x$.
*   **Trigonometric Functions:**
    *   `math.sin(x)`, `math.cos(x)`, `math.tan(x)`: Return the sine, cosine, and tangent of $x$ (in radians), respectively.
    *   `math.degrees(x)`: Converts angle $x$ from radians to degrees.
    *   `math.radians(x)`: Converts angle $x$ from degrees to radians.
    *   `math.asin(x)`, `math.acos(x)`, `math.atan(x)`: Return the inverse sine, inverse cosine, and inverse tangent of $x$ (in radians), respectively.
    *   'math.dist(p,q): dist between 2 points p and q
    *   `math.hypot(*coordinates)`: Returns the Euclidean norm of a vector or the distance from the origin to a point.
*   **Other Special Functions:**
    *   `math.factorial(x)`: Returns the factorial of $x$.
    *   `math.isfinite(x)`, `math.isinf(x)`, `math.isnan(x)`: Check if $x$ is finite, infinite, or Not a Number, respectively.

### Insights or Next Steps

*   The `math` module is an indispensable tool for scientific computing and numerical analysis in Python, providing efficient implementations of common mathematical operations.
*   Further exploration could involve implementing practical problems using a combination of these functions, such as calculating statistical measures, solving geometric problems, or performing financial calculations.
"""

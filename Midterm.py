import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    result = round(math.pi * radius ** 2, 2)
    return result

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):

    result = ""
    row = 1

    while row <= n:

        if n <= 3:
            return "The triangle height should be at least 4."

        else:

            if row == 1:
                peak = "*" + "\n"
                result += peak
                row += 1

            if row == 2:
                body = "*" + "*" + "\n"
                result += body
                row += 1

            if row > 2 and row < n:
                while row <= n:
                    body = "*" + " " * (row - 2) + "*" + "\n"
                    result += body
                    row += 1
            
            if row == n:
                base = "*" * n
                result += base

    return result


# Q3: Inverted Pyramid
def inverted_pyramid(n):

    result = ""

    if n <= 2:
        return "The pyramid height should be at least 3."

    else:
        for i in range (n, 0, -1):
            space = " " * (n - i)
            stars = "*" * (2 * i - 1)
            result += space + stars + "\n"

        return result.strip()


# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()

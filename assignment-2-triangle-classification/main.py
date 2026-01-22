def classify_triangle(a, b, c):
    sides = sorted([a, b, c])
    x, y, z = sides # we always treat the largest side as the hypotenuse (z) which is why we sort

    if x <= 0 or y <= 0 or z <= 0:
        return "invalid"
    if x + y <= z:
        return "invalid"

    if a == b == c:
        kind = "equilateral"
    elif a == b or b == c or a == c:
        kind = "isosceles"
    else:
        kind = "scalene"

    is_right = (x * x + y * y) == (z * z)
    if is_right:
        return f"right {kind}"
    return kind


def main():
    print(classify_triangle(3, 4, 5))


if __name__ == "__main__":
    main()

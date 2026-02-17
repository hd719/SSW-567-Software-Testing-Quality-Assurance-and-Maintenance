"""Triangle classification program for SSW-567 assignment 2."""


def classify_triangle(a, b, c):
    """Classify a triangle by side lengths, including right-triangle detection."""
    sides = sorted([a, b, c])
    # We always treat the largest side as the hypotenuse (z), so we sort first.
    x, y, z = sides

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
    """Run a simple example classification."""
    print(classify_triangle(3, 4, 5))


if __name__ == "__main__":
    main()

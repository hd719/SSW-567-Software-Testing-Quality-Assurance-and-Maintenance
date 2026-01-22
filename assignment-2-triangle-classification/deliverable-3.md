# Questions

## What challenges did you encounter with this assignment, if any?

- I’ve only touched Python testing a little before, so the biggest challenge was getting used to pytest’s syntax and how tests are typically organized. I also had to slow down and make sure the triangle rules were right, especially the validity checks (positive sides and the triangle inequality).

## What did you think about the requirements specification for this assignment?

- The requirements were clear about triangle types and the right‑triangle rule. The only gray area was what to do with invalid inputs (zero, negative, or failing the triangle inequality), so I chose to return "invalid" for those cases.

## What challenges did you encounter with the tools?

- The tooling itself wasn’t too bad, but I did have to make sure pytest could find my tests (naming matters). I also tweaked some assertions after a few runs to make sure the expected outputs matched what the function should return.

## Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?

I felt done once I covered every classification (equilateral, isosceles, scalene, right), invalid inputs (zero/negative sides and triangle inequality problems), and a few edge cases like reordering the sides for right triangles. After those all passed and I couldn’t think of any missing boundaries, it felt complete.

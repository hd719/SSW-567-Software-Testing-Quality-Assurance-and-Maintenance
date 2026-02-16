# Questions

## What did you think about when designing the code to make it easy to test?

When I build integrations or work with APIs, I try to keep things simple and easy to test. Instead of writing one big function that does everything, I split the work into smaller pieces: one function just finds the user’s repositories, another only counts commits for a specific repo, and a third function simply ties those two steps together. That way, each part can be tested on its own without everything being tangled up. I also keep the formatting in a separate function so the logic and the "pretty output" don’t depend on each other if the formatting changes later, it won’t break the core behavior, and vice versa.

## What challenges did you face while testing this assignment?

The biggest challenge was GitHub API rate limiting: during repeated test runs I hit requests.exceptions.HTTPError: 403 Client Error: rate limit exceeded on <https://api.github.com/users/hd719/repos>, which showed that live API-based tests can fail even when the code itself is correct.

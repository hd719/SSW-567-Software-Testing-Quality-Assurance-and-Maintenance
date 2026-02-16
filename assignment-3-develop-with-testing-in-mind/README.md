# HW 03a: Develop with Testing in Mind

## How to Run

From this folder (`assignment-3-develop-with-testing-in-mind`):

```bash
cd assignment-3-develop-with-testing-in-mind
uv sync
uv run python github_api.py hd719
```

Example test run:

```bash
uv run pytest -q
```

If you are using `pip` instead of `uv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install requests pytest
python github_api.py hd719
pytest -q
```

Developing with the Perspective of the Tester in mind
Background:
This assignment will require that you write code to interface with an external REST-based APIs.   We could have used almost any external APIs, but for this assignment we chose GitHub because many of its APIs are public and do not require any authorization or API Keys.   This simplifies both the use and setup.

For this assignment imagine that you have been asked to develop a function that will interface with GitHub in order to extract and present useful information to your user. The function will communicate using the RESTful services APIs provided by GitHub. The GitHub APIs will allow you to query for information about users, repositories, etc... which can be retrieved using the function, and then be displayed in the application.

What should make this assignment different from other programming assignments is in how you will approach it.  You should approach this assignment as a developer who more than anything else has the perspective of the tester in the front of your mind.

The developer looks at the requirements and asks how should I design and implement this function, but the tester will ask questions such as what will I need to test for in this function?  And how will I test this function?   As you design and write the function as a developer, you should consider the perspective of the tester in any of your design and implementation decisions.   One deliverable of this assignment will be to reflect and comment on this.

Note:  we will be building on this assignment for next week, so you will definitely need to complete this assignment this week.

Requirements:
You should write a function that will take as input a GitHub user ID.
The output from the function will be a list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories.

So, for example, if user John567 has 2 repositories named "Triangle567" and "Square567" each with some number of commits, then the function might output :

Repo: Triangle567 Number of commits: 10
Repo: Square567 Number of commits: 27
Implementation requirements:
You should implement the application in Python 3.X, same as what you have been using for other assignments.

Retrieving a user's repositories:

To retrieve a user's list of repositories you can use this GitHub API:

<https://api.github.com/users/><ID>/repos
Given a user <ID>, this API will return a list of JSON objects, one for each repositories for that user.  The "Name:" attribute of the JSON object will be the name of the repo.

For example, for the user "richkempinski" the URL would be:

<https://api.github.com/users/richkempinski/repos>
Put this URL into your browser to see the list of json results that are returned.  You should see that one of the repositories returned has the name "hellogitworld"

Retrieving the commits of a repository:

To retrieve the commits for a specific user repository, use this API:

<https://api.github.com/repos/><ID>/<REPO>/commits
This API will take a user <ID> and the name of the <REPO> and will return a list of JSON objects, one object for each commit. All you need to do is count how many element are in this list to know the number of commits.

For example, for the user "richkempinski" and for the repository "hellogitworld" then th e URL would be:

<https://api.github.com/repos/richkempinski/hellogitworld/commits>
Put this URL into the browser to see the list of commits for the repo.

Recommended Modules:

You should use these modules in your program to make requests and to handle the results.

import requests
The requests module can be used to request data from the GitHub API service.

import json
The json module can be used to parse the json response data from the GitHub API.

Important:
The purpose of this assignment is NOT about writing a complex or pretty function.  This should be a simple implementation, and in fact, the implementation is small relative to the Triangle programming assignment.  But think about how you will test the function and how you can make testing easy to implement.
Design and write the program in a way that will make it easy for anyone to test.

In addition to the function you should also include some unit tests similar to how you tested the Triangle program in HW 02a to prove to yourself that the program is behaving correctly.

The application code should be saved in a new folder on GitHub repository you used for the previous assignment.   Give this new folder a meaningful name.   For example, the name could be something like GitHubApi567-hw4a

Link this application to Travis-ci or Circle-CI to make it part of CI process. You can add an additional test command for the HW4a in your .yml file without having to remove the one from HW2b.

Note that if you use the "requests" module you may need to install this package with pip.

Deliverables:
You have 2 deliverables for this assignment:

1. The GitHub URL to the repository containing your code.
You should link this application to Travis-ci or Circle-CI to make sure that the code builds.  The README should contain a badge that indicates that the build is successful and that your tests pass, Follow the same pattern as was done in the previous assignment.

Your grade for this part will be on having a complete program that meets the requirements and which demonstrates a correct result.
2. Write a description of what you thought about when you were designing the code.  What did *you* think was important to do to make it easy to test the program.  What are some of the challenges that you faced when testing this assignment.

---

Mock the GitHub API
In assignment HW 03a you may have encountered problems when testing your code in Travis-CI given that your tests were highly dependent on the GitHub APIs. Those APIs would start to return errors if you exceeded a threshold on use, or those APIs would return different results if you made a change to your repos. Remember that one of the key concepts behind unit-tests was that if you don't change your program then the unit-tests should behave consistently. Unfortunately, that is not the case so far.

In this assignment you will use a mocking package to "mock" your program's external dependence on GitHub, so that you can guarantee that your unit tests will run consistently every time you run them, no matter how many times you run them, and no matter what changes you make to your repos.

Instructions
Start with the GitHub API program that you completed in "HW 03a:" and mock out all of the service calls in that program using the python mock module.

For this assignment you won't need to create any new repository; instead, you will make all of your changes in the same repository that you used for HW 3a.   In order to separate what you do in this assignment from what you did in HW 3a, we will make use of git branching.  For HW 03a all of your code should be on the "master" branch of your repository.  For this assignment you will make all of your changes on a different branch named "HW03c_Mocking".   You will need to create this new branch.

You can either create the branch locally on your laptop and then push the branch and its associated changes up to GitHub, or you can create the branch in GitHub and pull that branch down to your local repository.    Once you have your new branch, then all changes for mocking your API calls should go on that branch.

Note that when you are making any changes to the programs on the "HW03a_Mocking" branch, that you should not make any changes to the program that is calling the GitHub APIs using the requests module.  Rather, all of your changes that you make in the "HW03a_Mocking" branch should be in two files:  (1) the file containing the unit tests, and (2) the README file.  The README file for the branch should be updated so that the badge shows the status of your unit tests for the code on the "HW03a_Mocking" branch.  If you don't make any changes to it then the badge will show the status of your code on the "master" branch.

When you are done you should then be able to run your tests on Travis-ci and it should not make any calls to GitHub.  You will have eliminated all dependencies to the GitHub APIs.

With Python 3, the mock package is already part of the unittest module as unittest.mock

Check out these links which might be useful to you:

<https://blog.fugue.co/2016-02-11-python-mocking-101.html>

<https://medium.com/python-pandemonium/python-mocking-you-are-a-tricksy-beast-6c4a1f8d19b2>

<https://realpython.com/blog/python/testing-third-party-apis-with-mocks/>

Deliverables:
Submit the GitHub URL of the repository containing your code (should be the same as what you submitted for HW 03a).  .   My expectation will be that

1. all of your changes for this assignment will be on the branch "HW03a_Mocking"

2. the README file will contain a badge that links to the build status of your code on the branch "HW03a_Mocking" running in Travis-CI.

3. the build status will be success

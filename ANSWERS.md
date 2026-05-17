# Theory Questions

### 1. What is the difference between unit tests, integration tests, regression tests and performance tests?
```commandline
Unit tests are used to verify that a small piece of code works correctly. They test isolated parts of the code, 
such as an individual function or method.
Integration tests are used to verify that different components work together and exchange data correctly. They 
test the interaction between modules, services, databases, or the user interface (UI).
Regression tests are done to ensure that existing functionality still works after changes are made. They test 
previously working features after new code has been added.
Performance tests are used to measure speed, stability, and resource usage. They test response time, 
scalability, load handling, and efficiency.
```

### 2. Describe how it works when working with TDD.
```commandline
In TDD, you always start with a unit test, such as testing addBook() or toggleFavorite() in isolation. 
You first write a failing test, then implement the simplest possible code to make it pass, 
and finally refactor while keeping the test green. This is the core TDD cycle: red → green → refactor.

As the system grows, you also add integration tests to check how components work together, for example:
“add a book, then toggle favorite, and verify the final state in the BookStore.” These are not the starting
point of TDD, but they extend the same principle of writing tests early to guide development.

Over time, your growing suite of unit and integration tests naturally becomes regression testing, since
rerunning them after every change ensures that existing functionality has not been broken.

Performance tests are different—they are usually not part of the TDD cycle. They are introduced separately
to measure speed, scalability, and resource usage, since TDD is primarily focused on correctness rather than
performance.

Therefore, TDD mainly starts with unit tests, while integration and regression testing naturally build on top
of it, and performance testing sits outside the core TDD process.

### 3. Describe how BDD differs from TDD.
```commandline
The main difference is that TDD focuses on code correctness at the unit level, meaning you test individual 
functions or methods to ensure they work as expected, while BDD focuses on system behavior from a user or 
business perspective, describing how the system should behave in real-world scenarios. Tools like Behave 
support BDD by allowing you to write readable Given/When/Then scenarios in natural language and then connect 
them to code, whereas TDD is usually written directly in test code without this natural language layer, 
focusing more on technical implementation details.
```

### 4. Imagine that you were going to make a website similar to the Reading List, both frontend and backend.
If you had to choose unconditionally, what kinds of tests would you want to use? Justify your choice.
```commandline
If I’m building a reading list app, I would choose integration testing for the backend and Playwright 
end-to-end (E2E) testing for the frontend because they give me the most realistic view of how the system 
works in practice.

For the backend, I prefer integration testing because features like adding a book, toggling favorite, 
and removing it involve different parts working together. I don’t just want to test a single function 
in isolation—I want to make sure the whole process works from start to finish and that the data is 
saved and updated correctly throughout the system.

For the frontend, I would use Playwright E2E testing because it lets me test the app the same way a 
real user interacts with it. I can simulate opening the app, adding a book through the UI, clicking 
favorite, and checking that everything updates correctly on the screen. This gives me confidence that 
the entire user journey works, including the connection between the UI and backend.
```
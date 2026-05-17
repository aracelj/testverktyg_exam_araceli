Feature: [U1] Mark book as favorite (heart click)


  Scenario Outline: Mark a book as favorite
      Given a list of books is displayed from the homepage catalog list
      When the user clicks the toggle icon on "The Pragmatic Procrastinator"
      Then the book "The Pragmatic Procrastinator" should be added to the favorites list
      And the toggle icon should appear selected
      And the number of favorite books should increase by 1

  Examples:
    | title                                    | author                   |
    | Snakes on a Plane: A Python Story        | Guido van Rossum         |
    | The Pragmatic Procrastinator             | Dave Thomasson           |

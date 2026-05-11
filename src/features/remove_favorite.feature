Feature: Remove Favorite Book


  Scenario Outline: Remove a favorite book
      Given the book "<title>" is marked as favorite
      And the statistics show 1 favorite book
      When the user clicks the heart icon for "<title>" 2 times
      Then the book "<title>" should no longer be marked as favorite
      And the book "<title>" should be removed from the favorites list
      And the statistics should show 0 favorite books

  Examples:
      | title                                    | author             |
      | Ormar på ett plan: En Python-berättelse  | Guido van Rossum   |
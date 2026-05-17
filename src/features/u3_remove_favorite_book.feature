Feature: [U3] Unmark a book as favorite from catalog


  Scenario Outline: User unmarks a favorite book
    Given a book "<title>" is already marked as favorite
    When the user toggles the heart icon for the favorite book "<title>"
    Then the book "<title>" is unmarked as favorite
    And the book "<title>" is removed from My Books list
    And the favorite count in statistics is decreased by 1

  Examples:
    | title                                    |
    | Ormar på ett plan: En Python-berättelse  |



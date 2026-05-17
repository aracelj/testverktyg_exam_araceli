Feature: [U5] Statistics List


Scenario Outline: User views statistics for books and favorites
    Given the user is on the homepage
    When the user opens the "Statistics" section
    Then the total number of books in the catalog should be "<total_books>"
    And the total number of favorite books should be "<total_fav_books>"

  Examples:
  | total_books | total_fav_books |
  | 13          | 0               |
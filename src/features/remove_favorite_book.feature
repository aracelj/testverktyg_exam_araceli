Feature: [U2] Removed favorite book


Scenario: User unmark a book from catalog list by clicking the heart icon again
    Given a book is already marked as favorite
    When the user clicks the heart icon again
    Then the book should be removed from the favorites list
    And the heart icon should appear unselected
    And the statistics should decrease by 1 favorite book

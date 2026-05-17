Feature: [U3] Add new book to catalog

Scenario: User adds a new book to the catalog
    Given the user is on the Add Book section
    When the user enters a title and author
    And the user submits the form
    Then the new book should appear in the catalog list
    And the catalog total count should equal the previous count plus 1
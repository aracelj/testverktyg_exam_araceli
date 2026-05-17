Feature: [U4] Add new book to catalog

Scenario Outline: User adds a new book to the catalog
    Given the user is on the Add Book section
    When the user enters a title and author
    And the user submits the form
    Then the new book should be added in the catalog list
    And the total number of books in the Statistics section is updated






Feature: [U1] Mark book as favorite (heart click)


  Scenario: User marks a book as favorite by clicking the heart icon
      Given the catalog contains a list of books
      When the user clicks the heart icon on a book
      Then the book should be added to the favorites list
      And the heart icon should appear selected
      And the statistics should increase by 1 favorite book


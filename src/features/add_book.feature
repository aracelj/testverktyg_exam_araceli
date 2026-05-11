Feature: Add Book

  Scenario: Add new book to the catalog
      Given the user is on the "Add New Book" tab
      When the user enters the title "The Hobbit"
      And the user enters the author "J.R.R. Tolkien"
      And the user clicks the "Add Book" button
      Then the book should be added to the catalog list
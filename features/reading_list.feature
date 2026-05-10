Feature: Reading List System

  Scenario: Mark book as favorite
      Given the user is viewing the homepage
      When the user clicks the heart icon next to a book
      Then the book should be marked as favorite
      And the selected book should display a heart icon next to its title


  Scenario: Add new book to the catalog
      Given the user is on the "Add New Book" tab
      When the user enters the title "The Hobbit"
      And the user enters the author "J.R.R. Tolkien"
      And the user clicks the "Add Book" button
      Then the book should be added to the catalog list


  Scenario: View My Books
      Given the user is on the homepage
      When the user clicks the "My Books" tab
      Then the user should see their list of favorite books


  Scenario: User views favorite books statistics
      Given the user is on the homepage
      When the user clicks the "Statistics" tab
      Then the user should see the number of books marked as favorites
Feature: Mark Favorite Book


  Scenario: Mark book as favorite
      Given the user is viewing the homepage
      When the user clicks the heart icon next to a book titled "The Pragmatic Procrastinator"
      Then the book should be marked as favorite
      And the selected book should display a favorite icon next to the title "The Pragmatic Procrastinator"



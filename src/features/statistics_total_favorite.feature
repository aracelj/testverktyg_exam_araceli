Feature: [U5] View Total Favorite Books Statistics

Scenario: User views favorite books statistics
      Given the user has favorite books in the system
      When the user opens the statistics section
      Then the number of favorite books should be displayed correctly
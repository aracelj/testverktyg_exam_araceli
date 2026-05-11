Feature: Favorite Book Statistics

  Scenario: User views the statistics
      Given the user is on the homepage
      When the user clicks the "Statistics" tab
      Then the user should see the number of books marked as favorites

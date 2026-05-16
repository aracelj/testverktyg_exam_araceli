Feature: Remove Favorite Book


  Scenario: Remove a favorite book
      Given the book "Git Blame and Other Ways to Lose Friends" is marked as favorite
      And the statistics show 1 favorite book
      When the user clicks the heart icon for "Git Blame and Other Ways to Lose Friends" 2 times
      Then the book "Git Blame and Other Ways to Lose Friends" should no longer be marked as favorite
      And the book "Git Blame and Other Ways to Lose Friends" should be removed from the favorites list
      And the statistics should show 0 favorite books

Feature: Remove Favorite Book


  Scenario: Remove a favorite book
      Given the book "Ormar på ett plan: En Python-berättels" is marked as favorite
      And the statistics show 1 favorite book
      When the user clicks the heart icon for "Ormar på ett plan: En Python-berättels"
      Then the book "Ormar på ett plan: En Python-berättels" should no longer be marked as favorite
      And the book "Clean Code" should be removed from the favorites list
      And the statistics should show 0 favorite books
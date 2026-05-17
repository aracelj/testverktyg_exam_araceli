Feature: [U6] View Total Books Statistics

Scenario: User views total books statistics
    Given the user has favorite books in the system
    When the user opens the statistics section
    Then the number of total books should be displayed correctly in the statistics section

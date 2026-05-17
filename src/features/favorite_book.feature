Feature: [U1] Mark book as favorite (heart click)


  Scenario Outline: Mark a book as favorite
      Given a list of books is displayed from the homepage catalog list
      When the user clicks the toggle icon on "<title>"
      Then the book "<title>" is marked as favorite

  Examples:
    | title                                    |
    | Ormar på ett plan: En Python-berättelse  |


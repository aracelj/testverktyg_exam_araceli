Feature: [U1] Mark book as favorite (heart click)


  Scenario Outline: User marks a book as favorite
  Given a book "<title>" is not marked as favorite
  When the user clicks the toggle icon for the book "<title>"
  Then the book "<title>" is marked as favorite

Examples:
  | title                                    |
  | Ormar på ett plan: En Python-berättelse  |
  | The Pragmatic Procrastinator             |


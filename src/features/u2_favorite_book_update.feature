Feature: [U2] My Books page

Scenario Outline: Favorite book is reflected in My Books and Statistics count
  Given a book "<title>" is marked as favorite
  When the user opens the My Books section
  Then the book "<title>" should be visible in the favorites list
  And the favorite count in statistics is increased by 1

Examples:
  | title                                    |
  | Ormar på ett plan: En Python-berättelse  |
  | The Pragmatic Procrastinator             |
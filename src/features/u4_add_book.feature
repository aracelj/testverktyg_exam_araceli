Feature: [U4] Add new book to catalog

Scenario Outline: User adds a new book to the catalog
  Given the user is on the catalog page
  When the user opens the "Add Book" section
  And the user enters a book with title "<title>" and author "<author>"
  And the user submits the form
  Then the book "<title>" by "<author>" should be added to the catalog list

Examples:
  | title                | author         |
  | Python Crash Course  | Eric Matthes   |
  | Clean Code           | Robert Martin  |




# Testverktyg Exam  
Submitted by Araceli Jakobsson
Github: https://github.com/aracelj/testverktyg_exam_araceli.git
Modules included:

Completed the following:
Backend:
A. Unit Test for All functions in BookStore and FavoriteBooks
```commandline
source : src/backend/booklist.py
Unit Test : python -m pytest tests/unit/test_booklist_unit.py
Integration Test : python -m pytest tests/integration//test_booklist_integration.py 
```

B. In root folder
```commandline
README.md
STORIES.md
ANSWERS.md
```

C. User Stories for Catalog, Add Book, My Books views.

D. Features
```commandline
Features:
    Catalog :  u1_favorite_book.feature
    Catalog/My Books/Statistics :  u2_favorite_book_update.feature
    My Books: u3_remove_favorite_book.feature
    Add Book : u4_add_book.feature
    Statistics : u5_statistics.feature
    
Steps:
    u1_favorite_book_steps.py
    u2_favorite_book_update_steps.py
    u3_remove_favorite_book_steps.py
    u4_add_book_steps.py
    u5_statistics_steps.py
```

E. Tests

```commandline
Backend (PASSED)
Frontend (PASSED) : 
        behave src/features/u1_favorite_book.feature  
        behave src/features/u2_favorite_book_update.feature   
        behave src/features/u3_remove_favorite_book.feature
        behave src/features/u4_add_book.feature  
        behave src/features/u5_statistics.feature    
```
  
F. Higher quality and code that is reused.
G. User stories that cover the Statistics view.
H. Page Object design pattern
```commandline
    catalog_page.py
    mybooks_page.py
    add_book_page.py
    stats_page.py
```
I. Scenario Outline
J. Other user stories features

from config import DATABASE_URI
from model import Author, Selection, SelectionDetails, Content
from tools import get_session_engine
from sqlalchemy import select, func
from sqlalchemy.orm import sessionmaker


def execute_query(session, query, print_results=False):
    results = session().execute(query).all()
    if print_results:
        for result in results:
            print(result)
        print('\n')
    return results


if __name__ == '__main__':
    sess, _ = get_session_engine(DATABASE_URI)

# Весь контент: «название контента», «раздел», «ник автора» «аннотация».
    all_content = select(Selection, Author.name, Content.name, Content.abstract).join(Author.contents).join(Content.selection)
    execute_query(sess, all_content, print_results=True)
    
# Все авторы: «ник автора», «email автора» «число постов».
    all_authors = select(Author.name, Author.email, func.count(Content.id)).join(Content).group_by(Author.id)
    execute_query(sess, all_authors, print_results=True)
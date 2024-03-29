from datetime import datetime
from random import choice, randint, sample

from tools import create_database
from sqlalchemy import select

from config import DATABASE_URI
from model import Author, Content, Selection



def fill_db(sess):
    def read_csv(filename):
        with open(f"./static_data/{filename}.csv", "r") as f:
            result = [line.strip() for line in f]
        return [r.split(";") for r in result]

    authors = read_csv("authors") # customers
    contents = read_csv("contents") # products
    selections = read_csv("selections") 


    with sess() as session, session.begin():
        for a in authors:
            auth = Author(name=a[0], email=a[1])
            session.add(auth)


        for s in selections:
            selec = Selection(name=s[0])
            session.add(selec)

    with sess() as session, session.begin():
        auth_id = [a.id for a in session.scalars(select(Author)).all()]

        for c in contents:
            cont = Content(author_id=choice(auth_id), \
                           name=c[0], abstract=c[3], fillings=c[4])

            for _ in range(randint(1, 5)):
                s = Selection(name=choice(selections)[0])
                cont.selections.append(s)
            session.add(cont)
            session.add(s)


if __name__ == "__main__":
    print("connecting...")
    session = create_database(DATABASE_URI)
    print("connection established")
    print("db created!")

    fill_db(session)
    print("db filled with data")
    
    session().close()
    print("session closed")



    # con = Content()
    # sel = Selection()
    
    # sel.details.append(con)
    # session.add(sel)
    # session.add(con)

    # with sess() as session, session.begin():
    #     cont_id = [c.id for c in session.scalars(select(Content)).all()]
    #     selec_id = [s.id for s in session.scalars(select(Selection)).all()]
    #     for i in range(4):
    #         select_det = SelectionDetails(selection_id=choice(selec_id), \
    #                                       content_id=choice(cont_id))
    #     for sd in cont_id:
    #         cont_pids = sample(selec_id, randint(1, 2))

    #         for sd2 in cont_pids:
    #             selec_det = SelectionDetails(content_id=sd, selection_id=sd2)
    #             session.add(selec_det)





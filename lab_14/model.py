from sqlalchemy import ForeignKey, Identity
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy.types import DateTime, Integer, Numeric, String
from sqlalchemy import Column
from sqlalchemy import Table

class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = 'author'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String(50), nullable=False)
    email = mapped_column(String, nullable=False)
    
    contents = relationship('Content', back_populates='author')

    def __repr__(self):
        return f'<Author: id={self.id}, name={self.name}, email={self.email}>'
    


selection_content = Table("selection_content", \
            Base.metadata, 
            Column("selection_id", ForeignKey("selection.id"), primary_key=True),\
            Column("content_id", ForeignKey("content.id"), primary_key=True)
)

class Content(Base):
    __tablename__ = 'content'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String, nullable=False)
    abstract = mapped_column(String, nullable=False)
    author_id = mapped_column(Integer, ForeignKey('author.id'), nullable=False)
    fillings = mapped_column(String, nullable=False)
    
    author = relationship('Author', back_populates='contents')
    selections = relationship('Selection', secondary="selection_content", back_populates='contents')
    
    def __repr__(self):
        return f'Content(id={self.id}, name={self.name}, abstract={self.abstract}, filling={self.fillings})'


class Selection(Base):
    __tablename__ = 'selection'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    contents = relationship('Content' ,secondary="selection_content", back_populates='selections')

    def __repr__(self):
        return f'Selection(id={self.id}, name={self.name})'


if __name__ == '__main__':
    from sqlalchemy.schema import CreateTable
    print(CreateTable(Author.__table__))
    print(CreateTable(Content.__table__))
    print(CreateTable(Selection.__table__))

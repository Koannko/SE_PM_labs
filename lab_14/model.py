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


class Content(Base):
    __tablename__ = 'content'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String, nullable=False)
    abstract = mapped_column(String, nullable=False)
    author_id = mapped_column(Integer, ForeignKey('author.id'), nullable=False)
    # selection_id = mapped_column(Integer, ForeignKey('selection.id'), nullable=False)
    fillings = mapped_column(String, nullable=False)
    
    author = relationship('Author', back_populates='contents')
    details = relationship('Selection', secondary="SelectionDetails", back_populates='details')
    # selection = relationship('Selection', back_populates='contents')
    
    def __repr__(self):
        return f'Content(id={self.id}, name={self.name}, abstract={self.abstract}, filling={self.fillings})'


class Selection(Base):
    __tablename__ = 'selection'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    details = relationship('Content' ,secondary="SelectionDetails", back_populates='details')
    # contents = relationship('Content', back_populates='selection')

    def __repr__(self):
        return f'Selection(id={self.id}, name={self.name})'


# class SelectionDetails(Base):
#     __tablename__ = 'selection_details'
#     selection_id = mapped_column(Integer, ForeignKey("selection.id"), primary_key=True)
#     content_id = mapped_column(Integer, ForeignKey("content.id"), primary_key=True)
#     quantity = mapped_column(Integer, nullable=False)
#     selection = relationship("Selection", back_populates="details")
#     content = relationship("Content", back_populates="details")


#     def __repr__(self):
#         return f'<Details: selection={self.selection_id}, content={self.content_id}, qty={self.quantity}>'
SelectionDetails = Table("SelectionDetails", \
            Base.metadata, Column("selection_id", Integer, ForeignKey("selection.id")),\
            Column("content_id", Integer, ForeignKey("content.id")),)

# association_table = Table(
#     'content_selection_association',
#     Base.metadata,
#     Column('content_id', Integer, ForeignKey('content.id')),
#     Column('selection_id', Integer, ForeignKey('selection.id'))
# )


if __name__ == '__main__':
    from sqlalchemy.schema import CreateTable
    print(CreateTable(Author.__table__))
    print(CreateTable(Content.__table__))
    print(CreateTable(Selection.__table__))

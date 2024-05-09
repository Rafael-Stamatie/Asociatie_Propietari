from sqlalchemy import (Column, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def new_session(db_file_path):
    engine = create_engine(f'sqlite:///{db_file_path}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session()


class Imobil(Base):
    __tablename__ = 'imobile'

    id = Column(String, primary_key=True)

    admin_nume = Column(String)
    admin_prenume = Column(String)
    admin_telefon = Column(String)
    admin_email = Column(String)

    presedinte_nume = Column(String)
    presedinte_prenume = Column(String)
    presedinte_telefon = Column(String)
    presedinte_email = Column(String)

    localitate = Column(String)
    strada = Column(String)
    numar = Column(String)


class Apartament(Base):
    __tablename__ = 'apartamente'

    id = Column(String, primary_key=True)

    numar = Column(String)
    numar_locatari = Column(Integer)
    imobil_id = Column(ForeignKey('imobile.id'))

    proprietar_nume = Column(String)
    proprietar_prenume = Column(String)

    index_apa = Column(Float)
    index_curent = Column(Float)
    index_gaz = Column(Float)

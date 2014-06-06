import sys, os
from sqlalchemy import Column, Integer, String, create_engine

pg_url = os.environ.get("DATABASE_URL", "postgres://latgayvifnbujx:tnmhWRaSDBDkXBxsfHvTLY2iyR@ec2-54-204-2-255.compute-1.amazonaws.com:5432/d825k9i6ka2tlt")
engine = create_engine(pg_url, echo=True)





class User(Base):
   __tablename__ = 'users'

   id = Column(Integer, primary_key=True)
   name = Column(String)
   fullname = Column(String)
   password = Column(String)

    def __repr__(self):
      return "<User(name='%s', fullname='%s', password='%s')>" % (
                          self.name, self.fullname, self.password)

if __name__ == "__main__":

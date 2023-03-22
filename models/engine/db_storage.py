#!/usr/bin/python3
""" New engine for SQL database """
import os
from sqlalchemy        import create_engine
from sqlalchemy.orm    import sessionmaker, relationship, scoped_session
from models.base_model import Base, BaseModel
from models.base_model import BaseModel
from models.user       import User
from models.state      import State
from models.review     import Review
from models.place      import Place
from models.amenity    import Amenity
from models.city       import City

class DBStorage:
    """ main database storage class """

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(os.getenv("HBNB_MYSQL_USER"),
                                                                            os.getenv("HBNB_MYSQL_PWD"),
                                                                            os.getenv("HBNB_MYSQL_HOST"),
                                                                            os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query everything from a class (or from everything if class is not specified) """
        allObjList = []
        if cls == None:
            """ Query all """
            #for obj in self.__session.query(User).all():
            #    allObjList.append(obj)
            for obj in self.__session.query(State):
                allObjList.append(obj)
            #for obj in self.__session.query(Review):
            #    allObjList.append(obj)
            #for obj in self.__session.query(Place):
            #    allObjList.append(obj)
            #for obj in self.__session.query(Amenity):
            #    allObjList.append(obj)
            for obj in self.__session.query(City):
                allObjList.append(obj)
        else:
            """ Query only the specified class """
            cls = eval(str(cls)) # transfo string -> class (i love you eval-sama)
            allObjList = self.__session.query(cls)

        ObjDict = {}
        for obj in allObjList:
            ObjDict["{}.{}".format(type(obj).__name__, obj.id)] = obj
        return ObjDict

    def new(self, obj):
        """ Add object to database """
        self.__session(obj)

    def save(self):
        """ commit """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete an object """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """ Create a session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
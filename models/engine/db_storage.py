import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """
    This class is responsible for storing and retrieving objects
    to and from the MySQL database.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new instance of the DBStorage class.
        Creates a new SQLAlchemy engine instance and
        sessionmaker instance
        """
        username = os.getenv('HBNB_MYSQL_USER')
        password = 0s.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(username, password,
                                              host, database),
                                      pool_pre_ping=True)
        if os.getenv('HBNH_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """
        Queries the database for objects of a specified class
        Return a dictionary of the queried objects
        """
        objects - {}
        if cls:
            for obj in self.__session.query(cls):
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for clazz in[BaseModel]:
                for obj in self.__session.query(clazz):
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """
        Adds new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to current database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all database tables from Base metadate
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

#!/usr/bin/env python3
"""DB module
"""
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """The method saves a user to the database
        """
        new_user = User()
        # Create a new User object
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the new user to the session
        session = self._session
        session.add(new_user)

        # Commit the session to save the user to the database
        session.commit()

        # Refresh the new_user instance to reflect the newly assigned ID
        session.refresh(new_user)

        # Return the newly created user
        return new_user

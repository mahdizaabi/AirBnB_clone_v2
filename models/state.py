#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    __tablename__ = "states"

    @property
    def cities(self):
        """[summary]
        Returns:
            [type]: [description]
        """
        cities_list = []
        for cts in models.storage.all(City).values():
            if cities.state_id == self.id:
                cities_list.append(cts)
        return cities_list

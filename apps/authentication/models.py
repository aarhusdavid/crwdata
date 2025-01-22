# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from datetime import datetime
from apps import db, login_manager

'''
Add your models below
'''

class cd_user(UserMixin, db.Model):
    __tablename__ = "cd_user"
    __table_args__ = {'schema': 'crwdata'}


    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    parent_location_id = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    last_login = db.Column(db.DateTime, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)


    def __init__(self, id, first_name, last_name, email, password, parent_location_id=None, role=None, last_login=None, is_admin=False):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.parent_location_id = parent_location_id
        self.role = role
        self.last_login = last_login
        self.is_admin = is_admin


    def __repr__(self):
        return f"<User {self.email}>"


class cd_parent_location(db.Model):
    __tablename__ = "cd_parent_location"
    __table_args__ = {'schema': 'crwdata'}


    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String,nullable=True)
    name = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=True)
    date_established = db.Column(db.Date, nullable=True)
    street_address_one = db.Column(db.String, nullable=True)
    street_address_two = db.Column(db.String, nullable=True)
    suite_building_number = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    zipcode = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    website_url = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    child_location_ids = db.Column(db.Text, nullable=True)

    def __init__(self, id, user_id=None, name=None, type=None, date_established=None, street_address_one=None, 
                 street_address_two=None, suite_building_number=None, city=None, state=None, zipcode=None, 
                 country=None, website_url=None, description=None, child_location_ids=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.type = type
        self.date_established = date_established
        self.street_address_one = street_address_one
        self.street_address_two = street_address_two
        self.suite_building_number = suite_building_number
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        self.website_url = website_url
        self.description = description
        self.child_location_ids = child_location_ids

    def __repr__(self):
        return f"<ParentLocation {self.name}>"


class cd_child_location(db.Model):
    __tablename__ = "cd_child_location"
    __table_args__ = {'schema': 'crwdata'}


    id = db.Column(db.String, primary_key=True)
    parent_location_id = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=True)
    date_established = db.Column(db.Date, nullable=True)
    street_address_one = db.Column(db.String, nullable=True)
    street_address_two = db.Column(db.String, nullable=True)
    suite_building_number = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    zipcode = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    website_url = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, id, parent_location_id=None, name=None, type=None, date_established=None, street_address_one=None, 
                 street_address_two=None, suite_building_number=None, city=None, state=None, zipcode=None, 
                 country=None, website_url=None, description=None):
        self.id = id
        self.parent_location_id = parent_location_id
        self.name = name
        self.type = type
        self.date_established = date_established
        self.street_address_one = street_address_one
        self.street_address_two = street_address_two
        self.suite_building_number = suite_building_number
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        self.website_url = website_url
        self.description = description

    def __repr__(self):
        return f"<ChildLocation {self.name}>"

@login_manager.user_loader
def user_loader(id):
    return cd_user.query.filter_by(id=id).first()


# from __future__ import annotations
#
# import hashlib
# import secrets
#
# from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, UniqueConstraint, MetaData
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.sql import func
#
# from python.database.fastcode import get_database_schema, get_database_engine, get_transaction
#
# engine = get_database_engine()
# metadata = MetaData(bind=engine, schema=get_database_schema())
# Base = declarative_base(metadata=metadata)
#
#
# class User(Base):
#     __tablename__ = 'user'
#     use_id = Column('use_id', Integer, nullable=False, autoincrement=True, primary_key=True)
#     use_username = Column('use_username', String, nullable=False, unique=True)
#     use_password_salt = Column('use_password_salt', String, nullable=False)
#     use_password = Column('use_password', String, nullable=False)
#     use_created_at = Column('use_created_at', TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
#     def __repr__(self):
#         return F"<User {self.use_id} {self.use_username}>"
#     # def __init__(self, session, use_id: str, password: str):
#     #     self.use_username = use_id
#     #     self.use_password_salt = secrets.token_hex(20)
#     #     self.use_password = hashlib.sha256(bytes(password + self.use_password_salt, 'UTF8')).hexdigest()
#     #     session.add(self)
#     # @classmethod
#     # def get_or_create(self, session, use_id: str, password: str):
#     #     user = User()
#     #     user.use_username = use_id
#     #     user.use_password_salt = secrets.token_hex(20)
#     #     user.use_password = hashlib.sha256(bytes(password + self.use_password_salt, 'UTF8')).hexdigest()
#     #     try:
#     #         session.add(user)
#     #         session.
#     #     except:
#     #         session.refresh(user)
#     #         session.query(User.use_id == )
#     #         session.add(self)
#
#
#
# class Token(Base):
#     __tablename__ = 'token'
#     tok_id = Column('tok_id', Integer, nullable=False, primary_key=True, autoincrement=True)
#     use_id = Column('use_id', Integer, ForeignKey(User.use_id), nullable=False, unique=True)
#     tok_token = Column('tok_token', String, nullable=False)
#     tok_token_type = Column('tok_token_type', String, nullable=False)
#     tok_token_scope = Column('tok_token_scope', String, nullable=False)
#     tok_token_expires_in = Column('tok_token_expires_in', Integer, nullable=False)
#     tok_token_refresh = Column('tok_token_refresh', String, nullable=False)
#     tok_token_expires_at = Column('tok_token_expires_at', Integer, nullable=False)
#     tok_last_updated_at = Column('tok_last_updated_at', TIMESTAMP(timezone=True), nullable=False,
#                                  server_default=func.now())
#
#     def __repr__(self):
#         return F"<Token {self.tok_id} from user {self.use_id}>"
#
#
# class Context(Base):
#     __tablename__ = 'context'
#     con_id = Column('con_id', Integer, nullable=False, primary_key=True, autoincrement=True)
#     con_type = Column('con_type', String, nullable=False)
#     con_uri = Column('con_uri', String, nullable=False, unique=True)
#
#     def __repr__(self):
#         return F"<Context {self.con_id}>"
#
#
# class History(Base):
#     __tablename__ = 'history'
#     his_id = Column('his_id', Integer, nullable=False, primary_key=True, autoincrement=True)
#     use_id = Column('use_id', Integer, ForeignKey(User.use_id), nullable=False)
#     tra_id = Column('tra_id', String, nullable=False)
#     his_played_at = Column('his_played_at', TIMESTAMP(timezone=True), nullable=False)
#     con_id = Column('con_id', Integer, ForeignKey(Context.con_id), nullable=True)
#     __table_args__ = UniqueConstraint('use_id', 'his_played_at'),
#
#     def __repr__(self):
#         return F"<History {self.his_id} at {self.his_played_at}>"
#
#
# class Device(Base):
#     __tablename__ = 'device'
#     dev_id = Column('dev_id', Integer, nullable=False, primary_key=True, autoincrement=True)
#     use_id = Column('use_id', Integer, ForeignKey(User.use_id), nullable=False)
#     dev_token = Column('dev_token', String, nullable=False)
#     dev_active = Column('dev_active', Boolean, nullable=False, default=False)
#     dev_created_at = Column('dev_created_at', TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
#
#     def __repr__(self):
#         return F"<Device {self.dev_id} from user {self.use_id}>"
#
#
# Base.metadata.create_all()
#
# if __name__ == "__main__":
#     pass

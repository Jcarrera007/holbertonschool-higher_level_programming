#!/usr/bin/python3
"""This module defines a State class and an instance Base = declarative_base().

Requirements:
- Uses SQLAlchemy's declarative system.
- Links the `State` class to the MySQL table `states`.
- Provides `id` (auto-generated PK, not null) and `name` (String(128), not null).
- When executed as a script, connects to a MySQL server on localhost:3306 and
    creates tables with Base.metadata.create_all(engine).

Note: Importing this module will NOT attempt to connect to the database; the
connection is only made when running this file directly to satisfy the
"connect to MySQL" requirement without side effects on import.
"""

import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states"""
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


def _build_engine_from_env():
    """Create a SQLAlchemy engine from environment variables.

    Expected environment variables:
    - MYSQL_USER: database username (required for connection)
    - MYSQL_PWD: database password (can be empty for no password)
    - MYSQL_HOST: database host (default: 'localhost')
    - MYSQL_PORT: database port (default: '3306')
    - MYSQL_DB:   database name (required for connection)

    Returns:
        sqlalchemy.Engine | None: an Engine if enough info is provided; otherwise None.
    """
    user = os.getenv("MYSQL_USER")
    pwd = os.getenv("MYSQL_PWD", "")
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    db = os.getenv("MYSQL_DB")

    # Only build engine if we have the essential parts
    if not user or not db:
        return None

    # Use MySQLdb driver (mysqlclient), commonly used in Holberton tasks
    url = f"mysql+mysqldb://{user}:{pwd}@{host}:{port}/{db}"
    return create_engine(url, pool_pre_ping=True)


if __name__ == "__main__":
    # WARNING: All classes inheriting from Base must be imported
    # before calling Base.metadata.create_all(engine).
    # In this module we only define `State`, so it's already imported.
    engine = _build_engine_from_env()
    if engine is None:
        # Provide a helpful hint without raising during direct execution
        print(
            "Missing DB info. Set MYSQL_USER and MYSQL_DB (optional: MYSQL_PWD, "
            "MYSQL_HOST, MYSQL_PORT) to create tables."
        )
    else:
        Base.metadata.create_all(engine)
        print("Tables ensured (create_all) on the configured database.")
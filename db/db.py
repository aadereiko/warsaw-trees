import psycopg2
from psycopg2 import OperationalError
from API import warsaw_trees
from service_data_transform import transform_service_dict

DB_NAME = 'warsaw_trees'
DB_USER = 'aadereiko'
DB_PASSWORD = '220699'
DB_PORT = '5432'
DB_HOST = 'localhost'

params = {
    "database": DB_NAME, "user": DB_USER, "password": DB_PASSWORD, "port": DB_PORT, 'host': DB_HOST
}


def create_health_state_type():
    sql_type = """CREATE TYPE health_state AS ENUM('good', 'medium', 'bad');"""
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(sql_type)
    except Exception as e:
        print(e)


def create_tree_db():
    tree_list = warsaw_trees.get_tree_list()
    print([(transform_service_dict(x)) for x in tree_list['result']['records'][:1]])

    sql_table = """CREATE TABLE trees(
        id integer PRIMARY KEY,
        x real NOT NULL,
        y real NOT NULL,
        x_pl real NOT NULL,
        y_pl real NOT NULL,
        inventory_number varchar(7),
        district varchar(100),
        unit varchar(100),
        city varchar(100),
        address varchar(200),
        location varchar(200),
        property_number varchar(100),
        species varchar(200),
        species_lat varchar(200),
        measurement_date date,
        age_d int,
        height_m float,
        stem_circumference varchar(20),
        crown_diameter float,
        health_state health_state
    )
    """
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(sql_table)
                conn.commit()
    except Exception as e:
        print(e)


def insert_trees_from_service_into_db():
    resp = warsaw_trees.get_tree_list()['result']['records']


def init_db():
    create_health_state_type()
    create_tree_db()
    insert_trees_from_service_into_db()


init_db()

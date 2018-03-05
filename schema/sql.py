# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection

from .base import TableBase, SchemaBase


class SqlTable(TableBase):
    """docstring for SqlTable"""
    def __init__(self, url, **kw):
        super(SqlTable, self).__init__(url, **kw)
        self.engine = create_engine(url)
        self.inspector = reflection.Inspector.from_engine(self.engine)

    """return list of column type dict, include defult value, auto increase 
       or not, type, name, nullable or not,etc.
       param: table, request table name
    """
    def get_columns(self, table):
        return self.inspector.get_columns(table)
        
    def get_row_count(self):
        pass

    """ Return information about primary key constraint on table_name.
        Given a string table_name, and an optional string schema, 
        return primary key information as a dictionary with these keys:
        constrained_columns
            a list of column names that make up the primary key
        name
            optional name of the primary key constraint.
    """
    def get_pk_constraint(self, table):
        return self.inspector.get_pk_constraint()

    """ Return information about unique constraints in table_name.
        Given a string table_name and an optional string schema, 
        return unique constraint information as a list of dicts with these keys:
        name
            the unique constraint’s name
        column_names
            list of column names in order
    """
    def get_unique_constraints(self):
        return self.inspector.get_unique_constraints()

    def get_statistic(self):
        pass

    def get_entry_type(self):
        pass

    def get_table_info(self):
    	table = {}
        table['statistic'] = self.get_statistic()
        table['entry_type'] = self.get_entry_type()

        return table

    def __str__(self):
        pass

class SqlSchema(SchemaBase):
    """docstring for SqlSchema"""
    def __init__(self, url, **kw):
        super(SqlSchema, self).__init__(url, **kw)
        self.engine = create_engine(url)
        self.inspector = reflection.Inspector.from_engine(self.engine)

    """return a list of table name"""        
    def get_tables(self):
        return self.inspector.get_table_names()

    """return a list of schema name"""
    def get_schema_names(self):
        return self.inspector.get_schema_names()

    def get_schema_info(self):
        schema = {}
        schema['table'] = self.get_table_info()
        return schema
# -*- coding: utf-8 -*-

class Statistic(object):
    """docstring for Statistic"""
    def __init__(self, url, **kw):
        self.url = url
        self.row_count = 0

    def get_row_count(self):
        pass
    
    def get_state(self):
        state = {}

    def is_exists(self, names):
    	pass

    def get_statistic(self):
    	statistic = {}
    	statistic['rowcount'] = self.get_row_count()
    	statistic['state'] = self.get_state()
    	return statistic

    def save(self):
    	pass

    def __str__(self):
        pass


class EntryType(object):
    """docstring for EntryType"""
    def __init__(self,  url, **kw):
        self.url = url

    def get_field_list(self):
        pass

    def get_field_names(self):
        pass

    def get_field(self, name):
        pass

    def get_charset(self):
        pass

    def is_nullable(self):
        pass

    def is_rollup(self, column):
        pass

    """ Return information about primary key constraint on table_name.
        Given a string table_name, and an optional string schema, 
        return primary key information as a dictionary with these keys:
        constrained_columns
            a list of column names that make up the primary key
        name
            optional name of the primary key constraint.
    """
    def get_pk_constraint(self):
        pass

    """ Return information about unique constraints in table_name.
        Given a string table_name and an optional string schema, 
        return unique constraint information as a list of dicts with these keys:
        name
            the unique constraint’s name
        column_names
            list of column names in order
    """
    def get_unique_constraints(self, table, **kw):
        pass

    def get_entry_type(self):
    	entry_type = {}
    	entry_type['field'] = self.get_field_list()
    	return entry_type

    def __str__(self):
        pass


class TableBase(object):
    """docstring for TableBase"""
    def __init__(self, url, **kw):
        self.url = url
        self.table = None

    def get_statistic(self):
        pass

    def get_entry_type(self):
        pass

    def get_table_info(self):
        table = {}
        table['entry_type'] = self.get_entry_type()
        table['statistic']  = self.get_statistic()
        return table


class SchemaBase(object):
    """docstring for SchemaBase"""
    def __init__(self, url, **kw):
        self.url = url
        
    def get_table(self, name):
        pass

    def get_table_names(self):
        pass

    def get_table_dict(self):
        pass

    def is_mutable(self):
        pass

    def snapshot(self, version):
        pass

    def get_table_info(self):
    	pass

    def get_schema_info(self):
        schema = {}
        schema['table'] = self.get_table_info()
        return schema

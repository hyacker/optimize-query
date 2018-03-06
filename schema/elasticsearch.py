# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

from .base import Statistic, EntryType, TableBase, SchemaBase


class ESStatistic(Statistic):
    """docstring for ESStatistic"""
    def __init__(self, url, **kw):
        super(ESStatistic, self).__init__(url, **kw)

    def get_state(self):
        pass
        
    def is_exists(self):
        pass


class ESEntryType(EntryType):
    """docstring for ESEntryType"""
    def __init__(self, url, **kw):
        super(ESEntryType, self).__init__(url, **kw)

    def get_mapping(self):
        pass

    def get_field_mapping(self):
        pass


class ESTable(TableBase):
    """docstring for ESTable"""
    def __init__(self, url, **kw):
        super(ESTable, self).__init__(url, **kw)
        hosts = ['%s:%s' % host for host in self.url['hosts']]
        self.es = Elasticsearch(hosts, )

    def get_mapping(self, names):
        return self.es.indices.get_mapping(names)

    def get_segments(self, names):
        return self.es.cat.get_segments(names)

    def validate_query(self):
        pass

    def get_statistic(self):
    	pass

    def get_entry_type(self):
    	pass

    def get_table_info(self):
    	table = {}
        table['statistic'] = self.get_statistic()
        table['entry_type'] = self.get_entry_type()

        return table


class ESSchema(SchemaBase):
    """docstring for ESSchema"""
    def __init__(self, url, **kw):
        super(ESSchema, self).__init__(url, **kw)
        hosts = ['%s:%s' % host for host in self.url['hosts']]
        self.es = Elasticsearch(hosts, )
        
    def get_indices(self, names):
        return self.es.indices(names)

    def get_schema_names(self):
    	pass

    def get_schema_info(self):
        schema = {}
        schema['table'] = self.get_table_info()
        return schema
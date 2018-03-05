# -*- coding: utf-8 -*-
from .elasticsearch import ESTable, ESSchema
from .sql import SqlTable, SqlSchema

from ..util.uri_parser import parse_uri

tableset = {
    'es': ESTable,
    'sql': SqlTable,
}

schemaset = {
    'es': ESSchema,
    'sql': SqlSchema
}

def get_statistic():
	pass


def get_entry_type():
	pass


def get_table_info(url, **kw):
    url_conf = parse_uri(url)
    if not url_conf['subschema'] and url_conf['schema'] in ('mysql', 'postgresql'):
        url_conf['subschema'] = url_conf['schema']
        url_conf['schema'] = 'sql'
    table_class = tableset[url_conf['schema']]
    return table_class(url, **kw).get_table_info()


def get_schema_info(url, **kw):
    url_conf = parse_uri(url)
    if not url_conf['subschema'] and url_conf['schema'] in ('mysql', 'postgresql'):
        url_conf['subschema'] = url_conf['schema']
        url_conf['schema'] = 'sql'
    schema_class = schemaset[url_conf['schema']]
    return schema_class(url, **kw).get_schema_info()


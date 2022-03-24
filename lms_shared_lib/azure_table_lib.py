from asyncio.log import logger
import imp
import logging
import uuid

from azure.cosmosdb.table.tableservice import TableService

logger = logging.getLogger(__name__)

"""
Limits:
    nom de la table: ^[A-Za-z][A-Za-z0-9]{2,62}$
    Taille d'une entité individuelle Jusqu'a 1 Mo, avec un maximum de 255 propriétés (y compris PartitionKey, RowKey et Timestamp)
    Taille de la PartitionKey Chaîne jusqu'à 1 Ko
    Taille de la RowKey Chaîne jusqu'à 1 Ko
"""

class TableLMS:
    """
    Class LMS pour faciliter l'accès à une table Azure Storage.

    1 instance par table

    La table est crée automatiquement si elle n'existe pas 
    """
    TABLE_NAME = None
    DEFAULT_PARTITION_KEY = None

    # https://github.com/Azure/azure-cosmos-table-python/tree/master/azure-cosmosdb-table

    def __init__(self, table_name: str=None, connection_string: str=None, default_partition_key: str=None) -> None:

        self.table_name = table_name or self.TABLE_NAME

        if not self.table_name:
            raise AttributeError("table_name parameter or TABLE_NAME class attribute is required")

        self.connection_string = connection_string

        self.default_partition_key = default_partition_key or self.DEFAULT_PARTITION_KEY

        self.table_service = TableService(connection_string=self.connection_string)

        # check si la table_name exist sinon ont le crée
        if not self.table_service.exists(self.table_name):
            self.table_service.create_table(self.table_name)

    # inserer des éléments dans la table Azure 
    def insert(self, row_key: str=None, partition_key: str=None, **payload):

        if not partition_key:
            partition_key = self.default_partition_key

        if not row_key:
            row_key = payload.pop('RowKey', None)

        if not row_key:
            row_key = str(uuid.uuid4())

        if not isinstance(partition_key, str):
            raise AttributeError("partition_key is not str type")
        if not isinstance(row_key, str):
            raise AttributeError("row_key is not str type")

        payload = payload.copy()
        payload["PartitionKey"] = partition_key
        payload["RowKey"] = row_key

        self.table_service.insert_entity(self.table_name, payload)
    
    # inserer or merge des éléments dans la table Azure 
    def insert(self, row_key: str=None, partition_key: str=None, **payload):

        if not partition_key:
            partition_key = self.default_partition_key

        if not row_key:
            row_key = payload.pop('RowKey', None)

        if not row_key:
            row_key = str(uuid.uuid4())

        if not isinstance(partition_key, str):
            raise AttributeError("partition_key is not str type")
        if not isinstance(row_key, str):
            raise AttributeError("row_key is not str type")

        payload = payload.copy()
        payload["PartitionKey"] = partition_key
        payload["RowKey"] = row_key

        self.table_service.insert_or_merge_entity(self.table_name, payload)

        return row_key

    def get_doc(self, row_key: str, partition_key: str=None, raise_error: bool=False):
        if not partition_key:
            partition_key = self.default_partition_key

        try:
            return self.table_service.get_entity(self.table_name, partition_key, row_key)
        except Exception as err:
            if raise_error:
                raise 
    
    def list_all(self, **queries):
        for doc in self.table_service.query_entities(self.table_name): # TODO: , filter=queries):
            yield doc

    # task = table_service.get_entity('tasktable', 'tasksSeattle', '001')
    # tasks = table_service.query_entities('tasktable', filter="PartitionKey eq 'tasksSeattle'")
    # table_service.delete_entity('tasktable', 'tasksSeattle', '001')
    # table_service.delete_table('tasktable')
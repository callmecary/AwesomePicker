import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors

import config as cfg

HOST = cfg.settings['host']
MASTER_KEY = cfg.settings['master_key']
DATABASE_ID = cfg.settings['database_id']
COLLECTION_ID = cfg.settings['collection_id']


print(HOST)

client = document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY})
db = next((data for data in client.ReadDatabases() if data['id'] == DATABASE_ID))
coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == COLLECTION_ID))
doc = next((doc for doc in client.ReadDocuments(coll['_self']) if doc['id'] == '1'))

newdocument = client.CreateDocument(coll['_self'],
        { 
          "strategy_id": "0",
          "symbol": "fake_symbol4",
          "action": "fake_action4",
          "moving": 0.4,
          "past90moving": 0.04
        })

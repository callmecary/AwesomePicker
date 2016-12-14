import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors
import strategies
import datetime
import config as cfg

HOST = cfg.settings['host']
MASTER_KEY = cfg.settings['master_key']
DATABASE_ID = cfg.settings['database_id']
COLLECTION_ID = cfg.settings['collection_id']


print(HOST)

client = document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY})
db = next((data for data in client.ReadDatabases() if data['id'] == DATABASE_ID))
coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == COLLECTION_ID))
#doc = next((doc for doc in client.ReadDocuments(coll['_self']) if doc['id'] == '1'))

pead_results = strategies.get_pead_quotes(datetime.datetime.today())

for result in pead_results:
    newdocument = client.CreateDocument(coll['_self'],result)


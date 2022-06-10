import redis
from redis.commands.search.field import TextField, NumericField
from redis.commands.search.indexDefinition import IndexDefinition
from redis.commands.search.query import Query

# Connect to a database
r = redis.Redis()

# Options for index creation
index_def = IndexDefinition(
                prefix = ["py_doc:"],
                score = 0.5,
                score_field = "doc_score"
)

# Schema definition
schema = ( TextField("title"),
           TextField("body"),
           TextField("url"),
           NumericField("visits")
)

# Create an index and pass in the schema
r.ft("py_idx").create_index(schema, definition = index_def)

# A dictionary that represents a document
doc1 = { "title": "RediSearch",
         "body": "RediSearch is a powerful indexing, querying, and full-text search engine for Redis",
         "url": "<https://redis.com/modules/redis-search/>",
         "visits": 108
}

doc2 = { "title": "Redis",
         "body": "Modules",
         "url": "<https://redis.com/modules>",
         "visits": 102,
         "doc_score": 0.8
}

# Add documents to the database and index them
r.hset("py_doc:1", mapping = doc1)
r.hset("py_doc:2", mapping = doc2)


# Search the index for a string; paging limits the search results to 10
result = r.ft("py_idx").search(Query("search engine").paging(0, 10))

# The result has the total number of search results and a list of
# documents
print(result.total)
print(result.docs)

# Delete the index; set delete_documents to True to delete indexed
# documents as well
r.ft("py_idx").dropindex(delete_documents=False)


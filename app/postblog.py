from pymongo import MongoClient
from datetime import datetime

# Define the MongoDB URI
mongo_uri = "mongodb://test_user:password@mongodb-service:27017"

# Create a MongoClient instance
client = MongoClient(mongo_uri)

# Get the blog database and posts collection
db = client.blog
posts = db.posts

print(f"Welcome to this blog created by 297, 323, 328, 330")

title = input("Title of the post: ")
author = input("Author of the post: ")

# Insert a record into the posts collection
post = {"title": title, "author": author, "createdAt": datetime.now() }
post_id = posts.insert_one(post).inserted_id

# Print the inserted record ID
print(f"The record with ID {post_id} has been inserted")

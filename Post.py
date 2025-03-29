from datetime import datetime

from mongoengine \
    import (Document, StringField, ReferenceField, ListField, EmbeddedDocument, EmbeddedDocumentField, CASCADE,
            DateTimeField, URLField)

from User import User

class Comment(EmbeddedDocument):
    content = StringField(required=True)
    name = StringField(max_length=120, required=True)
    created_at = DateTimeField(default=datetime.utcnow)  # Timestamp for comments

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    meta = {
        'allow_inheritance': True,
        'indexes': ['author', 'tags'],  # Indexing for performance
        'collection': 'posts'
    }

class TextPost(Post):
    content = StringField(required=True)

class ImagePost(Post):
    image_path = StringField(required=True)

class LinkPost(Post):
    link_url = URLField(required=True)  # Ensures valid URL format

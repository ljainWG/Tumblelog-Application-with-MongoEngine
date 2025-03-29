from mongoengine import Document, StringField, DateTimeField, EnumField
from enum import Enum

class GenderEnum(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class User(Document):
    first_name = StringField(required=True,max_length=50)
    last_name = StringField(required=True,max_length=50)
    email = StringField(required=True, unique=True, regex=r"^[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook|watchguard|wg)\.com$")
    gender = StringField(required=True, choices=[e.value for e in GenderEnum])  # Enum field
    password = StringField(required=True, max_length=50, regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]{8,50}$")
    dob = DateTimeField(required=True)
    meta = {"collection": "users"}
    # meta = {
    #     "collection": "users",
    #     "ordering": ["-name"],  # Default ordering by name (descending)
    #     "indexes": ["email"],  # Create an index on email
    #     "strict": False  # Allows additional fields not defined in the model
    # }
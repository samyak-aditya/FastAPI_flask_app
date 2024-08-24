from bson import ObjectId
from pydantic import BaseModel, Field
from pydantic.json import ENCODERS_BY_TYPE

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, schema, field):
        schema.update(type="string")

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

# Make sure ObjectId is serializable
ENCODERS_BY_TYPE[ObjectId] = str

class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    email: str

    class Config:
        json_encoders = {ObjectId: str}

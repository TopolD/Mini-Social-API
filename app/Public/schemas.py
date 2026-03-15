from enum import Enum

from pydantic import BaseModel, ConfigDict


class PublicSchema(BaseModel):
    title: str
    content: str

    model_config = ConfigDict(from_attributes=True)


class PublicUpdateS(BaseModel):
    title: str | None = None
    content: str | None = None

    model_config = ConfigDict(from_attributes=True)


class SearchS(BaseModel):
    title: str | None = None
    content: str | None = None

    model_config = ConfigDict(from_attributes=True)


class SortField(str, Enum):
    sort = "created_at"
    like = "like_count"


class OrderField(str, Enum):
    desc = "desc"
    asc = "asc"

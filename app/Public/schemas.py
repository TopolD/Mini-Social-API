from pydantic import BaseModel, ConfigDict


class PublicSchema(BaseModel):
    title: str
    content: str

    model_config = ConfigDict(from_attributes=True)


class PublicUpdateS(BaseModel):
    title: str | None = None
    content: str | None = None

    model_config = ConfigDict(from_attributes=True)

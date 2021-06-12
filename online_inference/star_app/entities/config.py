from marshmallow_dataclass import dataclass, class_schema
# from marshmallow import fields

@dataclass
class ModelFields:
    temperature: int
    luminocity: float
    radius: float
    magnitude: float
    type: int
    color: str


modelFieldsSchema = class_schema(ModelFields)()

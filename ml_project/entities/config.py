from marshmallow_dataclass import dataclass, class_schema

@dataclass
class DataPathes:
    fin: str
    fout: str

DataPathesSchema = class_schema(DataPathes)


@dataclass
class Model:
    store_path: str
    n_estimators: int
    criterion: str
    max_depth: int
    target_col: str
    test_size: float
    random_state: int

ModelSchema = class_schema(Model)
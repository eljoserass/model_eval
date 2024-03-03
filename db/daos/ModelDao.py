from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Model import Model


class ModelDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Model | None:
        model = self.session.query(Model).filter(Model.uuid == uuid).first()
        return model
    
    def get_by_name(self, name: str) -> Model | None:
        model = self.session.query(Model).filter(Model.name == name).first()
        return model
    
    def get_all(self) -> list[Model]:
        models = self.session.query(Model).all()
        return models

    def create(self, model_data: dict) -> Model:
        model = Model(**model_data)
        print(model)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

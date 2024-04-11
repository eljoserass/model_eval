from sqlalchemy.orm import Session as SQLSession
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Session_Model import Session_Model


class Session_ModelDao(BaseDao):
    def __init__(self, session: SQLSession) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Session_Model | None:
        session_model = self.session.query(Session_Model).filter(Session_Model.uuid == uuid).first()
        return session_model
    
    def get_by_ids(self, session_id: int, model_id: int):
        session_models = self.session.query(Session_Model).filter(Session_Model.session_id == session_id).filter(Session_Model.model_id == model_id).first()
        return session_models
    
    def get_all(self) -> list[Session_Model]:
        session_model = self.session.query(Session_Model).all()
        return session_model

    def create(self, session_model_data: dict) -> Session_Model:
        session_model = Session_Model(**session_model_data)
        print(session_model)
        self.session.add(session_model)
        self.session.commit()
        self.session.refresh(session_model)
        return session_model

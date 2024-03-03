from sqlalchemy.orm import Session as SQLSession
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Session import Session


class SessionDao(BaseDao):
    def __init__(self, session: SQLSession) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Session | None:
        session_obj = self.session.query(Session).filter(Session.uuid == uuid).first()
        return session_obj
    
    def get_by_name(self, name: str) -> Session | None:
        session_obj = self.session.query(Session).filter(Session.name == name).first()
        return session_obj
    
    def get_all(self) -> list[Session]:
        session_obj = self.session.query(Session).all()
        return session_obj

    def create(self, session_data: dict) -> Session:
        session_obj = Session(**session_data)
        print(session_obj)
        self.session.add(session_obj)
        self.session.commit()
        self.session.refresh(session_obj)
        return session_obj

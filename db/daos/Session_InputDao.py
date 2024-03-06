from sqlalchemy.orm import Session as SQLSession
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Session_Input import Session_Input


class Session_InputDao(BaseDao):
    def __init__(self, session: SQLSession) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Session_Input | None:
        session_input = self.session.query(Session_Input).filter(Session_Input.uuid == uuid).first()
        return session_input
    
    def get_all(self) -> list[Session_Input]:
        session_input = self.session.query(Session_Input).all()
        return session_input

    def create(self, session_input_data: dict) -> Session_Input:
        session_input = Session_Input(**session_input_data)
        print(session_input)
        self.session.add(session_input)
        self.session.commit()
        self.session.refresh(session_input)
        return session_input

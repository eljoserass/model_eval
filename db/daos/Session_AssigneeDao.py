from sqlalchemy.orm import Session as SQLSession
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Session_Assignee import Session_Assignee


class Session_AssigneeDao(BaseDao):
    def __init__(self, session: SQLSession) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Session_Assignee | None:
        session_assignee = self.session.query(Session_Assignee).filter(Session_Assignee.uuid == uuid).first()
        return session_assignee
    
    def get_all(self) -> list[Session_Assignee]:
        session_assignee = self.session.query(Session_Assignee).all()
        return session_assignee

    def create(self, session_assignee_data: dict) -> Session_Assignee:
        session_assignee = Session_Assignee(**session_assignee_data)
        print(session_assignee)
        self.session.add(session_assignee)
        self.session.commit()
        self.session.refresh(session_assignee)
        return session_assignee

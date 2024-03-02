from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Session import Session


class SessionDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Session | None:
        session = self.session.query(Session).filter(Session.uuid == uuid).first()
        return session
    
    def get_all(self) -> list[Session]:
        session = self.session.query(Session).all()
        return session

    def create(self, session_data: dict) -> Session:
        session = Session(**session_data)
        print(session)
        self.session.add(session)
        self.session.commit()
        self.session.refresh(session)
        return session

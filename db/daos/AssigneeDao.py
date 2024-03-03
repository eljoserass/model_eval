from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Assignee import Assignee


class AssigneeDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Assignee | None:
        assignee = self.session.query(Assignee).filter(Assignee.uuid == uuid).first()
        return assignee
    
    def get_by_name(self, name: str) -> Assignee | None:
        assignee = self.session.query(Assignee).filter(Assignee.name == name).first()
        return assignee

    def create(self, assignee_data: dict) -> Assignee:
        assignee = Assignee(**assignee_data)
        print(assignee)
        self.session.add(assignee)
        self.session.commit()
        self.session.refresh(assignee)
        return assignee

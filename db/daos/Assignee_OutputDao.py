from sqlalchemy.orm import Session as SQLSession
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Assignee_Output import Assignee_Output


class Assignee_OutputDao(BaseDao):
    def __init__(self, session: SQLSession) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Assignee_Output | None:
        assignee_output = self.session.query(Assignee_Output).filter(Assignee_Output.uuid == uuid).first()
        return assignee_output
    
    def get_all(self) -> list[Assignee_Output]:
        assignee_output = self.session.query(Assignee_Output).all()
        return assignee_output

    def create(self, assignee_output_data: dict) -> Assignee_Output:
        assignee_output = Assignee_Output(**assignee_output_data)
        print(assignee_output)
        self.session.add(assignee_output)
        self.session.commit()
        self.session.refresh(assignee_output)
        return assignee_output

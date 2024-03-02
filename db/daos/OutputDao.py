from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Output import Output


class OutputDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Output | None:
        output = self.session.query(Output).filter(Output.uuid == uuid).first()
        return output
    
    def get_all(self) -> list[Output]:
        output = self.session.query(Output).all()
        return output

    def create(self, output_data: dict) -> Output:
        output = Output(**output_data)
        print(output)
        self.session.add(output)
        self.session.commit()
        self.session.refresh(output)
        return output

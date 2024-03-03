from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Input import Input


class InputDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Input | None:
        input = self.session.query(Input).filter(Input.uuid == uuid).first()
        return input
    
    def get_all(self) -> list[Input]:
        input = self.session.query(Input).all()
        return input

    def create(self, Input_data: dict) -> Input:
        input = Input(**Input_data)
        print(input)
        self.session.add(input)
        self.session.commit()
        self.session.refresh(input)
        return input

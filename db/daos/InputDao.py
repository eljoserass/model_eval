from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Input import Input
from sqlalchemy.sql.expression import func


class InputDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Input | None:
        input = self.session.query(Input).filter(Input.uuid == uuid).first()
        return input
    
    def get_with_limit(self, limit: int | None, shuffle: bool = False) -> list[Input]:
        if shuffle:
            input = self.session.query(Input).order_by(func.random()).limit(limit).all()
        else:
            input = self.session.query(Input).limit(limit).all()
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

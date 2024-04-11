from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Evaluation import Evaluation
from sqlalchemy.sql.expression import func


class EvaluationDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Evaluation | None:
        evaluation = self.session.query(Evaluation).filter(Evaluation.uuid == uuid).first()
        return evaluation
    
    def get_all(self) -> list[Evaluation]:
        evaluation = self.session.query(Evaluation).all()
        return evaluation

    def create(self, Evaluation_data: dict) -> Evaluation:
        evaluation = Evaluation(**Evaluation_data)
        print(evaluation)
        self.session.add(evaluation)
        self.session.commit()
        self.session.refresh(evaluation)
        return evaluation

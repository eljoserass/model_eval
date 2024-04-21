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
    
    def get_by_session_model_input_prompt_id(self, session_id: int, model_id: int, input_id: int, prompt_id: int) -> Output | None:
        output = self.session.query(Output).filter(Output.session_id == session_id).filter(Output.model_id == model_id).filter(Output.input_id == input_id).filter(Output.prompt_id == prompt_id).first()
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

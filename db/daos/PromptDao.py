from sqlalchemy.orm import Session
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Prompt import Prompt


class PromptDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Prompt | None:
        prompt = self.session.query(Prompt).filter(Prompt.uuid == uuid).first()
        return prompt
    
    def get_all(self) -> list[Prompt]:
        prompts = self.session.query(Prompt).all()
        return prompts

    def create(self, prompt_data: dict) -> Prompt:
        prompt = Prompt(**prompt_data)
        print(prompt)
        self.session.add(prompt)
        self.session.commit()
        self.session.refresh(prompt)
        return prompt

from sqlalchemy.orm import Session as SQLSession
from sqlalchemy import not_
from db.daos.BaseDao import BaseDao
from db.models.Session_Prompt import Session_Prompt


class Session_PromptDao(BaseDao):
    def __init__(self, session: SQLSession) -> None:
        super().__init__(session)

    def get_by_uuid(self, uuid: str) -> Session_Prompt | None:
        session_prompt = self.session.query(Session_Prompt).filter(Session_Prompt.uuid == uuid).first()
        return session_prompt
    
    def get_all(self) -> list[Session_Prompt]:
        session_prompt = self.session.query(Session_Prompt).all()
        return session_prompt

    def create(self, session_prompt_data: dict) -> Session_Prompt:
        session_prompt = Session_Prompt(**session_prompt_data)
        print(session_prompt)
        self.session.add(session_prompt)
        self.session.commit()
        self.session.refresh(session_prompt)
        return session_prompt

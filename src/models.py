from sqlalchemy.orm import Mapped
from src.database import Base

class CaseModel(Base):
    __tablename__ = "cases"

    tag: Mapped[str]
    case: Mapped[str]
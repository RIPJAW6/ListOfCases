from sqlalchemy.orm import mapped_column, Mapped
from src.database import Base

class CaseModel(Base):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    case: Mapped[str]
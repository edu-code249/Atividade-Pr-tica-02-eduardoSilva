from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(string = 200)
    pais: Mapped[str] = mapped_column(string = 200)

    livros = relationship("livro",back_populates="autor")


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(string = 200)
    ano: Mapped[int] = mapped_column(int = 200)
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    disponivel_id: Mapped[bool] = mapped_column(default=True)
    autor = relationship("Autor",back_populates="livros")


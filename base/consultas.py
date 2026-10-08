from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    # TODO: use select(Livro) e acesse livro.autor.nome.
    
    listar = select(Livro).join(Autor)
    return session.execute(listar).scalars().all()


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    # TODO: filtre Livro.disponivel igual a True.
    
    listando = select(Livro).where(disponível = True)
    return session.execute(listando).scalars().all()

def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    # TODO: use contains ou like no título.
    
    listname = select(Livro).where(Livro.titulo.contains(trecho))
    return session.execute(listname).scalars().all()


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.
    
    listnameautor = select(Autor).where(Autor.nome == nome_autor)
    autor = session.execute(listnameautor).scalars().first()
    return autor.livros if autor else []


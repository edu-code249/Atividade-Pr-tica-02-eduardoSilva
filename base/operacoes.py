from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    emprestar = select(Livro).where(Livro.titulo == titulo)
    livro = session.execute(emprestar).scalars().first()

    if not livro:
        print(f"Erro: O livro '{titulo}' não foi encontrado no sistema.")
        return

    if not livro.disponivel:
        print(f"Aviso: O livro '{titulo}' já está emprestado (indisponível).")
        return

    livro.disponivel = False
    session.commit()
    print(f"Sucesso: O livro '{titulo}' foi emprestado com sucesso!")

    """Marque um livro como indisponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver indisponível, exiba uma mensagem.
    # TODO: se estiver disponível, altere disponivel para False e faça commit.



def devolver_livro(session, titulo):
    devolver = select(Livro).where(Livro.titulo == titulo)
    livro = session.execute(devolver).scalars().first()

    if not livro:
        print(f"Erro: O livro '{titulo}' não foi encontrado no sistema.")
        return

    if livro.disponivel:
        print(f"Aviso: O livro '{titulo}' já está disponível no sistema.")
        return

    livro.disponivel = True
    session.commit()
    print(f"Sucesso: O livro '{titulo}' foi devolvido com sucesso!")
    
    """Marque um livro como disponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver disponível, exiba uma mensagem.
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.

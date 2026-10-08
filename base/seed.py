from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    
    autor1 = Autor(nome="J.R.R. Tolkien",pais="Inglaterra")
    autor2 = Autor(nome="George R.R. Martin",pais="Estados Unidos da América")
    autor3 = Autor(nome="J.K. Rowling",pais="Inglaterra")
    
    livro1 = Livro(titulo="O Hobbit", ano = 1937, autor=autor1, disponivel= False)
    livro2 = Livro(titulo="O Senhor dos Anéis", ano= 2001, autor=autor1)
    
    livro3 = Livro(titulo="A Guerra dos Tronos", ano = 2011, autor=autor2)
    livro4 = Livro(titulo="A Fúria dos Reis", ano = 1998, disponivel= False)
    
    livro5 = Livro(titulo="Harry Potter e a Pedra Filosofal", ano = 1991, disponivel= False)
    livro6 = Livro(titulo="Harry Potter e a Câmara Secreta", ano = 1993, autor=autor3)
    
    autor1.livros.extend([livro1, livro2])
    autor2.livros.extend([livro3, livro4])
    autor3.livros.extend([livro5, livro6])
    
    session.add_all([
        autor1, autor2, autor3,
        livro1, livro2, livro3, livro4, livro5, livro6
    ])

    session.commit()
    

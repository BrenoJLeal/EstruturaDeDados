class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
info = Livro('Cleancode','Robert Cecil' )
print(info.detalhes())
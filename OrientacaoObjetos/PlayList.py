class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    '''Funções do like'''
    def dar_like(self):
        self._likes += 1
    @property
    def likes(self):
        return self._likes
    '''Funções do nome'''
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    '''Funções que imprime as informações'''
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.likes}"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temp - {self.likes} likes"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]


    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme("Vingadores - Guerra infinita", 2018, 106)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")
for programa in playlist_fim_de_semana:
    print(programa)
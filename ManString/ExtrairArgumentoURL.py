class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválido!!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extraiArgumentos()
        representacaoString = f"Valor:{self.extraiValor()}\n" \
                              f"Moeda Origem: {moedaOrigem}\n" \
                              f"Moeda Destino: {moedaDestino}"
        return representacaoString

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def urlEhValida(url):
        if url and url.startswith("https://www.bytebank.com.br"):
            return True
        else:
            return False

    def extraiArgumentos(self):
        buscaMoedaOrigem  = "moedaorigem="
        buscaMoedaDestino = "moedadestino="

        indiceInicialMoedaOrigem    = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem  = self.encontraIndiceFinal(indiceInicialMoedaOrigem)

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino    = self.encontraIndiceFinal(indiceInicialMoedaDestino)

        moedaOrigem  = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()

            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.encontraIndiceFinal(indiceInicialMoedaOrigem)
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        return moedaOrigem,moedaDestino

    def encontraIndiceInicial(self, moedabuscada):
        return self.url.find(moedabuscada) + len(moedabuscada)

    def encontraIndiceFinal(self, indiceInicial):
        return self.url.find("&", indiceInicial)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]

        return valor
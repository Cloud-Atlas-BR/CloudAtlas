import json
import requests


class CamaraFederal():

    def __init__(self):
        self.version = "v2"
        self.base = "https://dadosabertos.camara.leg.br/api"

    def create_query(self, parameters):
        args = dict((k, v) for k, v in parameters.items() if v is not None)
        query = '&'.join("%s=%s" % (str(k), str(v)) for (k, v) in args.items())
        return query

    def listar_proposicoes(self, **kwargs):
        """Lista informações básicas sobre projetos de lei, resoluções,
           medidas provisórias, emendas, pareceres e todos os outros tipos de
           proposições na Câmara.

        Args:
            dataInicio (str): Data de início para listagem das proposições.
            dataFim (str): Data de fim para listagem das proposições.

        Returns:
            dict: Listagem de proposições retornadas

        """
        rota = "proposicoes"
        query = self.create_query(kwargs)
        endpoint = f"{self.base}/{self.version}/{rota}?{query}"
        response = requests.get(url=endpoint)
        content = json.loads(response.content.decode("UTF-8"))
        return content, response

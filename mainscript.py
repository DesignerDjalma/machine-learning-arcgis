

import arcpy
from getpass import getuser
from typing import List

import os


# Operação mais comum dentro de todo o código ✅
def operacaoPadrao():
    """Retorna mxd, cmds e dfs"""
    mxd = arcpy.mapping.MapDocument("current")
    cmds = arcpy.mapping.ListLayers(mxd)
    dfs = arcpy.mapping.ListDataFrames(mxd)
    return mxd, cmds, dfs


# Retorna um dict { nome_camada:camada } ✅
def dicionarioCamadas():
    _, lyr, _ = operacaoPadrao()
    cmds = { cmd.name:cmd for cmd in lyr }
    return cmds


# Converte um texto em um arcpy.mapping.Layer object ✅
def string2map(nome_da_camada):
    """Convert o nome da camada no objeto tipo map"""
    cmds = dicionarioCamadas()
    return cmds[nome_da_camada]






#⌛
class Caminhos:

    """ Os caminhos que serão usados. """
    area_de_trabalho : str = ""


#⌛
class Mascara:

    """ Para recortar futuramente. """

    def __init__(self, shape_interesse) -> None:
        self.shape_interesse = shape_interesse


#⌛
class Rasters:

    """ As imagens. """

    imagens : List[str] = []
    composicao : str = ""

    #⌛
    def gerarImagemComposicao(self, workspace: str) -> None:
        """ Gera a composicao com as Bandas. """

        saida_composicao: str = os.path.join(workspace, 'composicao.tif')
        arcpy.management.CompositeBands(self.composicao, saida_composicao)
        self.composicaoDataSource: str = saida_composicao
    
    #⌛
    def extrairPorMascara(self, on_shape, in_raster):
        pass


#⌛
def setupComposicao(lista_imagens: List[str]) -> None:
    """ Realiza o setup das imagens. """

    rasters.composicao: str = ";".join(lista_imagens)


#⌛
def configuraAmbiente(caminhos: Caminhos) -> None:
    """ Configura. """

    pass

    
    
    


#⌛
if __name__ == "__main__":

    # Instanciar as classes
    caminhos: Caminhos = Caminhos() ✅
    rasters: Rasters = Rasters() ✅

    # ✅
    caminhos.area_de_trabalho: str = "C:\\Users\\{}\\Documents\\testeDeImagens".format(getuser())
    rasters.imagens: List[str] = [
        "T22MHC_20220724T133851_B02.jp2",
        "T22MHC_20220724T133851_B03.jp2",
        "T22MHC_20220724T133851_B04.jp2",
        ]


    setupComposicao(rasters.imagens) # ✅
    rasters.gerarImagemComposicao(caminhos.area_de_trabalho) # ⌛ gerado só extrair
    shape_interesse: str = "shape de teste" ⌛
    camada_composicao: arcpy.mapping.Layer = string2map('composicao') ⌛
    rasters.extrairPorMascara(shape_interesse) ⌛

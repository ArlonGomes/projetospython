import os
import shutil


caminhoPasta = "C:/Users/Arlon/Documents/ProjetosIMG/"

imgs = os.scandir(caminhoPasta)

for imagem in imgs:
    imagemNome = imagem.name

    imagemExtencao = imagemNome[(imagemNome.__len__() - 3) : imagemNome.__len__()]
    if os.path.exists(caminhoPasta + imagemExtencao) != True:
        os.makedirs(caminhoPasta + imagemExtencao)
        
    shutil.move(caminhoPasta + imagemNome, caminhoPasta + imagemExtencao + "/")


    
# API-League-of-Legends
API para obter imagens de campeões

## Baixar repositório
```
git clone https://github.com/ricksfelix/API-League-of-Legends
```

## Instalação de Dependencias:
```bash
pip install -r requirements. txt
```
## Atualizar/Baixar Imagens
Execute o [scrap.py](https://github.com/ricksfelix/API-League-of-Legends/blob/main/scrap.py)

Nesta etapa, ele verificará o [champ_list.txt](https://github.com/ricksfelix/API-League-of-Legends/blob/main/champ_list.txt), após isso ele verificará se não há nem uma imagem faltando. após isso ele irá baixar as imagens dos campeões.


```
python scrap.py
```
## Informações Úteis
- `Square` = Icone do campeão
- `Splash` = Banner Original do campeão
- `Centered` = Banner porem com foco no campeão
- `p` = Icone da Passiva
- `q` = Icone da habilidade "Q"
- `w` = Icone da habilidade "W"
- `e` = Icone da habilidade "E"
- `r` = Icone da habilidade "R"

## Execução da API

> ## **EM BREVE**

## Documentações Utilizadas:
 - [Communit Dragon](https://www.communitydragon.org/documentation)
 - [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
 - [io](https://docs.python.org/3/library/io.html#io.BytesIO)
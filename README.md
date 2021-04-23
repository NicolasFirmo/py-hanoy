# py-hanoy
Visualizador das torres de hanoi

## Setup

Primeiramente não esqueçam de criar o ambiente virtual e instalar as dependências:
```shell
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Uso

Inicialize uma sessão instanciando um objeto `Hanoi` do arquivo [hanoi.py](./hanoi.py).
Não equeça de setar a função de desenho cena.

> ex

```py
hanoi = Hanoi(3)
Scene.set_draw_func(hanoi.draw)  # necessário para renderizar a torre na tela
```

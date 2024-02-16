# Python Django App GT (EM DESENVOLVIMENTO)
Aplicação Django para multi-projetos.

## Dependencias
- Python ^3.12;
- Poetry ^1.7.1;
- Node.js ^20.11.0 (LTS/Iron);

## Como usar
Feito todos os passos abaixo, o site vai estar disponivel na url [http://localhost:3000](http://localhost:3000).
> Os itens de 1 a 3 só precisam ser executado na primeira vez. 

### 1. Instalando a aplicação
1.1. É necessario fazer a instalação das dependencias do Python:
```sh
python -m venv .venv && poetry env use .venv/bin/python && poetry install
```
1.2. É necessario instalar as dependencias do Node.js (na pasta `www`):
```sh
npm install
``` 

### 2. Instalar migrations
2.1. Na pasta raiz do projeto, executar o comando:
```sh
python manage.py migrations
```

### 3. Iniciar servidor
3.1. Na pasta raiz do projeto, executar o comando:
```sh
python manage.py runserver
```
> O site vai estar disponivel na url: [http://localhost:8000](http://localhost:8000). Porem, recomendo seguir para o proximo passo.

### 4. Iniciar o build watch dos assets
4.1. Na pasta `www`, executar o comando:
```sh
npm run watch
```
Feito isso, vai iniciar o navegador com a url: [http://localhost:3000](http://localhost:3000) com todos os assets construidos.


## Dicas
- [Django Cheat Sheet](https://github.com/lucrae/django-cheat-sheet)

# Desafio de back-end utilizando Python/Django

### O Desafio:
Implementar uma API padrão RESTful utilizando Django, para o sistema de cotação de peças para Droids.


###Dependência:
<ul>[Docker](https://www.docker.com/get-started)

###Instalação:
1 - Gere um .env local (Esse passo pode ser feito de forma manual também, caso sua máquina não tenha o python instalado localmente, passo 1.1)
```sh 
python utils/env_gen.py 
```
1.1 - Crie um arquivo .env no caminho raiz e insira as seguintes variáveis
* DEBUG=True
* SECRET_KEY=Your$eCretKeyHere
* DB_NAME=postgres
* DB_USER=postgres
* DB_PASSWORD=postgres
* DB_HOST=db
 

2 - Iniciar os componentes da stack do projeto.
```sh 
docker-compose up
```
Nesse ponto você deve ter o projeto Django executando na porta 8000
http://localhost:8000

2 - Executar as migrações.:
```sh
docker-compose run web python manage.py migrate
```

3 - Criar primeiro usuário administrador:
```sh
docker-compose run web python manage.py createsuperuser
```

4 - (opcional) Importar lista de Estados brasileiros
```sh
docker-compose run web python manage.py import_states
```

5 - (opcional) Executer testes
```sh
docker-compose run web python manage.py test
```

###Implementações:
* Autenticação, cadastro e login para o anúnciante
* Lançamento de demanda
* Configuração do Django admin para o administrador do sistema

Todas as urls e formato de objetos que devem ser enviados para api estão na documentação, utilizada Postman aqui(https://documenter.getpostman.com/view/9411050/TVCjySLe)

######Observações:
Foi utilizado o model e permissões padrões de User para determinar se é admin ou anunciante. 

#Que a força esteja com você! 
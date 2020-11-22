<p style="color:red; font-size:20px;">Para atualizações posteriores ao prazo do projeto, verificar branch <b>delay</b></p>


# Pipeline for Metagenomics analysis

## How to compose this docker project

### Steps

1. Clone from github

```
$ git clone https://github.com/esthercamilo/compose16SMiSeq.git
```

2. To start the application

```
docker-compose up -d  
```

3. Access the container

a) Display docker running containers:

```
 docker ps  
```

b)Get the CONTAINER ID <number> of your django app and log into :

```
docker exec -t -i <number> bash  
```

3. Set up postgres/django database

```
docker-compose up -d  
```
4. Make migrations

```
python manage.py makemigrations
python manage.py migrate  
```


5. Create a superuser to access the application

```
python manage.py createsuperuser  
```

5. Deploy application

```
python manage.py runserver  
```





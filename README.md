# README

This is a simple demo of Django and DRF frame.

## 1. Deploy

1. First, go into fixes_demo folder.

![Untitled](README/Untitled.png)

1. If this is the first time deploy this server, You need to uncomment the `env_file` setting in `docker-compose-local.yml` file.

![Untitled](README/Untitled%201.png)

1. Before you run the docker-compose command, if you want to use your own python index url, you can replace script 2 with script 1, and replace the url after `-i` . 

![Untitled](README/Untitled%202.png)

1. Run the docker-compose command in fixes_demo folder:

```bash
docker-compose --verbose -f docker-compose-local.yml up
```

![Untitled](README/Untitled%203.png)

1. If you can see this, the server is up and running.

![Untitled](README/Untitled%204.png)

1. Type the address `[localhost:8000](http://localhost:8000)` in your browser, then you can get this.

![Untitled](README/Untitled%205.png)

## API Test

Product API:

1. Create product: use the `POST` method to send a request to `[localhost:8000/products/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%206.png)

![Untitled](README/Untitled%207.png)

1. Get all product: use the `GET` method to send a request to `[localhost:8000/products/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%208.png)

Variant API:

1. Create variant: use the `POST` method to send a request to `[localhost:8000/variants/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%209.png)

![Untitled](README/Untitled%2010.png)

![Untitled](README/Untitled%2011.png)

1. Get all variant: use the `GET` method to send a request to `[localhost:8000/variants/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%2012.png)

Image API:

1. Create image: use the `POST` method to send a request to `[localhost:8000/images/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%2013.png)

1. Get all image: use the `GET` method to send a request to `[localhost:8000/images/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%2014.png)

1. Get image by using id: use the `GET` method to send a request to `[localhost:8000/images/<id>/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%2015.png)

1. Update image: use the `PUT` method to send a request to `[localhost:8000/images/<id>/](http://localhost:8000/products/)` 

![Untitled](README/Untitled%2016.png)

This action will also update Product info and Variant info, to link Products/Variants to Image.

![Untitled](README/Untitled%2017.png)

![Untitled](README/Untitled%2018.png)

Filter and Sorting:

1. Filter:

Can use filter like this format: 

1. `localhost:8000/url/?<field>=<filter_value>`
2. `localhost:8000/url/?<field>__<key_word>=<filter_value>`

Char field can use the following key word:

```bash
'iexact',
'startswith',
'istartswith',
'endswith',
'iendswith',
'contains',
'icontains',
```

Date time field can the following key word:

```bash
'year',
'year__gt',
'year__lt',
'month',
'month__gt',
'month__lt',
'day',
'day__gt',
'day__lt',
```

![Untitled](README/Untitled%2019.png)

![Untitled](README/Untitled%2020.png)

![Untitled](README/Untitled%2021.png)

1. Sorting:

Can use filter like this format: 

1. Ascending: `localhost:8000/url/?sorting=<sorting_field>`

![Untitled](README/Untitled%2022.png)

1. Descending: `localhost:8000/url/?sorting=-<sorting_field>`

![Untitled](README/Untitled%2023.png)

1. Can use both filtering and sorting by using `&`.

![Untitled](README/Untitled%2024.png)

![Untitled](README/Untitled%2025.png)

## Addition:

This server can also supply get the API documentation in `localhost:8000/swagger/`

![Untitled](README/Untitled%2026.png)

OR [`localhost:8000/redoc/`](http://localhost:8000/redoc/)

![Untitled](README/Untitled%2027.png)
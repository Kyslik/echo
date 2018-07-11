# echo

> web-server, post, python, repeater, echoer

A web-server that echoes back POST requests with 200 status code.

## Using via docker


```shell
docker run -it --rm kyslik-/echo
```

or

```shell
docker run -it --rm kyslik/echo python echo.py -p 1234
```

or 

```shell
docker run -it --rm -d -p 1234:1234 kyslik/echo python echo.py -p 1234
```

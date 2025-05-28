programa para comunicacion entre 2 nodos inaccesibles (ips privadas) mediante la intermedacion de un tercer o broker con ip publica.

Nota, en el vps con ip publica debe correr el broker (con docker)

docker run -d --name rabbitmq   -p 5672:5672 -p 15672:15672   -e RABBITMQ_DEFAULT_USER=jose   -e RABBITMQ_DEFAULT_PASS=soCorongo_74   rabbitmq:3-management


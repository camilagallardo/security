
PASSWORDS:="$(PWD)/passwords"

build:
	docker build --rm -f Dockerfile -t password-playground .


run-shell:
	docker run -it --user="root" -v "$(PASSWORDS)":/var/passwords password-playground /bin/sh

down:
	docker stop $$(docker ps -a -q --filter "ancestor=password-playground") && docker rm $$(docker ps -a -q --filter "ancestor=password-playground")

attach:
	docker exec -it $$(docker ps -a -q --filter "ancestor=password-playground") /bin/sh

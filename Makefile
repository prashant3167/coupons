postgres:
	docker-compose --file docker-compose-postgres.yml up -d

couchbase:
	docker-compose --file docker-compose.yml up -d --remove-orphans

mongo:
	docker-compose --file docker-compose-mongo.yml up -d

start:
	docker-compose --file docker-compose-postgres.yml up -d
	docker-compose --file docker-compose.yml up -d
	docker-compose --file docker-compose-mongo.yml up -d

stop:
	docker-compose --file docker-compose-postgres.yml down
	docker-compose --file docker-compose.yml down
	docker-compose --file docker-compose-mongo.yml down


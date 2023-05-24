postgres: ## Run postgres
	@docker run -d -p 5432:5432 \
                  -e POSTGRES_PASSWORD=postgres \
                  -e POSTGRES_USER=postgres \
                  -e POSTGRES_DB=finder_db \
                  --name finder_db \
                  --restart always \
                  postgres:13;

redis:
	@docker run --name finder_redis \
                -p 6379:6379 \
                -d redis;



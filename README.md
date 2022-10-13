**<h1 style="text-align: center">Carford Car Shop</h1>**

System to manage car-related data into a database. The description lies below:

> Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small town, so the mayor had a bright idea to limit the number of cars a person may possess. One person may have up to 3 vehicles. The vehicle, registered to a person, may have one color, ‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
> Carford car shop want a system where they can add car owners and cars. Car owners may not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the system without owners.

# Setting the project up

## Docker Compose

Clone this repository and execute:

```bash
docker compose up -d
```

## CLI

It is also possible to run each of the parts manually, be it through the CLI or individual docker containers. For that, set up a MySQL container by executing:

```bash
docker run \
    --rm \
    -d \
    -p 3306:3306 \
    -v $PWD/db/scripts/start-up.sql:/docker-entrypoint-initdb.d/init.sql \
    -v $PWD/db/data-volume:/var/lib/mysql \
    -e MYSQL_DATABASE='Norktowndb' \
    -e MYSQL_USER='user' \
    -e MYSQL_PASSWORD='password_user' \
    -e MYSQL_ROOT_PASSWORD='password_root' \
    --network='norktownnetwork' \
    --restart='unless-stopped' \
    --name='advicehealth-db' \
    mysql:latest
```

Afterwards, set up the application container by executing*:

```bash
docker build -t advicehealth-api:latest .

docker run \
    --rm \
    -p 5000:5000 \
    --env-file=./.env \
    --name='advicehealth-api' \
    --network='norktownnetwork' \
    advicehealth-api:latest
```

*<sub>For the connection with the database to work properly when running the containers manually, change the "db" value in `SQLALCHEMY_DATABASE_URI` at the `settings.toml` to <b>"localhost"</b></sub>

# Usage

Feel free to browse the frontend at [http://localhost:5000](http://localhost:5000), and to access the API endpoints at [http://localhost:5000/api/v1/](http://localhost:5000/api/v1/).

---

**[GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html)**

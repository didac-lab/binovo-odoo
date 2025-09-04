# Odoo 16 CE — Custom Addons with Docker Compose

Stand up an Odoo 16 Community stack with PostgreSQL using Docker Compose and load a local **custom add-ons** directory.

## What’s included

* **Odoo 16 CE** service
* **PostgreSQL** database service
* **Mounted custom add-ons** at `/mnt/extra-addons`
* **odoo.conf** for centralized configuration

## Repository layout

```
.
├── docker-compose.yml
├── config/
│   └── odoo.conf
├── addons/
└── docs/
```

## Prerequisites

* Docker ≥ 20.x
* Docker Compose plugin ≥ 2.x

## Quick start

1. **Clone**

   ```bash
   git clone https://github.com/didac-lab/binovo-odoo.git
   cd binovo-odoo
   ```
2. **Start services**

   ```bash
   docker compose up -d
   ```
3. **Initialize Odoo**

   * Open [http://localhost:8069](http://localhost:8069)
   * Log in with **username:** `admin` and **password:** `admin`
   * Navigate to **Apps**, clear all default filters, then search and install the required modules (Blog, CRM, Sales)
   * Verify that `addons/` is correctly included in the `addons_path`

## Configuration

Use `config/odoo.conf` for centralized configuration:

```
[options]
admin_passwd = admin
addons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons
limit_time_cpu = 600
limit_time_real = 1200
```

## docker-compose.yml (reference)

```yaml
services:
  db:
    image: postgres:16
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

  odoo:
    image: odoo:16.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./config:/etc/odoo
      - ./addons:/mnt/extra-addons
    command: odoo -d odoo_db --dev=xml --db_user=odoo --db_password=odoo --db_host=db

volumes:
  odoo-web-data:
  odoo-db-data:
```

## Logs and troubleshooting

```bash
# Tail Odoo logs
docker compose logs -f odoo

# Tail Postgres logs
docker compose logs -f db
```

## License

This project is licensed under the [MIT License](LICENSE)

## Contact

If you have any questions or suggestions, feel free to contact us at [148581386+rwxce@users.noreply.github.com](mailto:148581386+rwxce@users.noreply.github.com).
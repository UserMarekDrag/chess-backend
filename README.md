# Chess platform

## Installation

1. Clone the repository:

    ```console
    git clone https://github.com/UserMarekDrag/chess-backend.git
    ```

2. Navigate to the directory:

    ```console
    cd chess-backend/
    ```

3. Copy the env file:

    ```console
    cp .env-example ./.env
    ```

4. Build and start the Docker services:

    ```console
    docker-compose up --build -d
    ```

5. The backend will be now running at <http://localhost:8082/>.

## Database Schema

![Database Schema](moviemate_visualized.png)

To generate a new database schema visualization, you can use the `django-extensions`'s `graph_models` command:

```console
python manage.py graph_models -a -o db-schema.png 
```

## Author

Marek Drąg

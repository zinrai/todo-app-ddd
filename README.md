# todo-app-ddd

Implements a simple TODO application using FastAPI and follows Domain-Driven Design (DDD) principles. It provides RESTful API endpoints for managing TODO items.

## Prerequisites

- Python 3.9+
- MySQL 8.0+

## Database Setup

Before running the application, you need to set up the MySQL database and user. Here are the commands to do so:

```
-- Connect to MySQL as root
$ mysql -u root -p
```

```sql
-- Create the database
CREATE DATABASE todo_app;

-- Create the user and grant privileges
CREATE USER 'todo_app'@'localhost' IDENTIFIED BY 'ra5cai7fei5U';
GRANT ALL PRIVILEGES ON todo_app.* TO 'todo_app'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
```

### Application Setup

Install dependencies:

```
$ pip install -r requirements.txt
```

Run the application:

```
$ uvicorn api.main:app --reload
```

## API Usage with cURL

Here are some example cURL commands to interact with the HTTP API:

```bash
# Create a new TODO item
curl -X POST "http://localhost:8000/todos" \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk, bread, and eggs"}'

# Get all TODO items
curl -X GET "http://localhost:8000/todos"

# Get a specific TODO item (replace {id} with actual ID)
curl -X GET "http://localhost:8000/todos/{id}"

# Update a TODO item (replace {id} with actual ID)
curl -X PUT "http://localhost:8000/todos/{id}" \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk, bread, eggs, and cheese", "completed": true}'

# Delete a TODO item (replace {id} with actual ID)
curl -X DELETE "http://localhost:8000/todos/{id}"
```

## Domain-Driven Design Implementation

This project follows Domain-Driven Design principles to structure the application. Here's an overview of how the domain is divided and implemented:

1. **Domain Layer**
   - Contains the core business logic and entities
   - Defined in `domain/models.py` and `domain/repositories.py`
   - `TodoItem` is the main entity representing a TODO item
   - `TodoRepository` is an abstract base class defining the interface for data persistence

2. **Application Layer**
   - Implements use cases and orchestrates the domain objects
   - Defined in `application/services.py`
   - `TodoService` class contains methods for creating, updating, deleting, and retrieving TODO items

3. **Infrastructure Layer**
   - Provides implementations for external concerns like databases
   - Defined in `infrastructure/repositories.py` and `infrastructure/database.py`
   - `MySQLTodoRepository` implements the `TodoRepository` interface for MySQL

4. **API Layer**
   - Handles HTTP requests and responses
   - Defined in `api/main.py`
   - Uses FastAPI to define endpoints that interact with the application layer

This structure allows for:

- Clear separation of concerns
- Isolation of the domain logic from external dependencies
- Easier testing and maintenance
- Flexibility to change the database or API framework without affecting the core business logic

The domain model (`TodoItem`) is at the center of the design, with other layers built around it. This ensures that the business rules are not dependent on UI, database, or any external agency.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.

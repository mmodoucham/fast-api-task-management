# Task Management App API Documentation

This repository contains a Task Management App API built using FastAPI and SQLite as the database. The API provides endpoints to manage tasks including creating, retrieving, updating, and deleting tasks.

## Project Setup

1. **Clone the Repository:**
   Clone this repository to your local machine using the following command:

```bash
    git clone https://github.com/mmodoucham/fast-api-task-management.git
```

2. **Install Dependencies:**
   Navigate to the project directory and install the required dependencies using pip:

```bash
cd fast-api-task-management/
pip install -r requirements.txt
```

3. **Run the API:**
   To run the api, navigate to the `apps` folder use the following command:

```bash
cd app/
python3 main.py
```

The API will be accesible on **`http://localhost:8000`**.

## API Endpoints

### Get All Tasks

- **Endpoint:** **`/tasks/`**
- **Method:** GET
- **Response:**

```json
{
  "code": "success",
  "status": 200,
  "response": [
    {
      "id": 1,
      "title": "Sample Task",
      "description": "This is a sample task",
      "dueDate": "2019-08-24T14:15:22Z"
    }
    // ... other tasks
  ]
}
```

### Create Task

- **Endpoint:** **`/tasks/`**
- **Method:** POST
- **Request:**

```json
{
  "parameter": {
    "title": "New Task",
    "description": "A new task",
    "dueDate": "2019-08-24T14:15:22Z"
  }
}
```

- **Response:**

```json
{
  "code": "success",
  "status": 201,
  "response": {
    "id": 5,
    "title": "New Task",
    "description": "A new task",
    "dueDate": "2019-08-24T14:15:22Z"
  }
}
```

### Get Task by ID

- **Endpoint:** **`/tasks/{task_id}`**
- **Method:** GET
- **Response:**

```json
{
  "code": "success",
  "status": 200,
  "response": {
    "id": 1,
    "title": "Sample Task",
    "description": "This is a sample task",
    "dueDate": "2019-08-24T14:15:22Z"
  }
}
```

### Update Task

- **Endpoint:** **`/tasks/`**
- **Method:**
- **Request:**

```json
{
  "parameter": {
    "title": "Updated Task",
    "description": "An updated task",
    "dueDate": "2019-08-24T14:15:22Z"
  }
}
```

- **Response:**

```json
{
  "code": "success",
  "status": 200,
  "response": {
    "id": 1,
    "title": "Updated Task",
    "description": "An updated task",
    "dueDate": "2019-08-24T14:15:22Z"
  }
}
```

### Delete Task

- **Endpoint:** **`/tasks/`**
- **Method:** DELETE
- **Response:**

```json
{
  "code": "success",
  "status": 204,
  "response": "task deleted"
}
```

## Testing the API with Swagger UI

Fast API comes with Swagger UI. This tool is automatically generated based on your API's route definitions and Pydantic models.

### Accessing Swagger UI

Once the API is running, Swagger UI can be accessed on the following URL:

```bash
http://localhost:8000/docs
```

You can use swagger UI to:

1. **Browse Endpoints**
2. **Send Requests**
3. **View Responses**
4. **Test Validations**

**To Test with SwaggerUI, you can do the following for each endpoint explained above**

1. Open your web browser and navigate to the /docs path as mentioned above.

2. Explore the available endpoints and select the one you want to test.

3. Click on the "Try it out" button to open an interactive form where you can input data.

4. Fill in the required parameters and request body (if applicable) according to the API documentation given above.

5. Click the "Execute" button to send the request to the API.

6. The response will be displayed below, showing the status code and response data.

7. You can also view example request and response payloads, which can be helpful for understanding the expected data format.

## Testing the API with pytest Framework

A suite of `tests` using the pytest framework was used to help verify the functionality of the Task Management App API.

### Running the tests

1. Navigate to the `tests` directory within your project using a terminal:

```bash
cd tests
```

2. Run the tests by executing the following command:

```bash
pytest
```

This command will automatically discover and run the test cases defined in the `test_app.py` file.

## Viewing API Documentation with ReDoc

FastAPI also provides an alternative way to view and interact with your API documentation using **ReDoc**, a tool that generates a sleek and responsive API documentation interface.

To view the API documentation using ReDoc, Open your web browser and navigate to the `/redoc` path:

```bash
http://localhost:8000/redoc
```

# Get Started 👨‍💻

👋 Welcome to Fast Mocker! This guide will walk you through the steps to install, run, and test the Fast Mocker project. Fast Mocker is a Python 3.11 project using FastAPI to simulate a REST API, returning responses based on YAML files in the `/mocks` folder.

## Installation 🚀

### Clone the Repository 🔗

To get started, you need to clone the Fast Mocker repository from GitHub. Open your terminal and run the following command:

```bash
git clone https://github.com/flaviofilipe/fast-mocker.git
```

### Install Dependencies with Poetry 📦

Fast Mocker uses Poetry to manage its dependencies. If you don't have Poetry installed, you can install it using `pip`:

```bash
pip install poetry
```

Next, navigate to the project folder and use Poetry to install the required dependencies:

```bash
cd fast-mocker
poetry install
```

## Running the Project ▶️

Now that the project is installed, you can run Fast Mocker using the following command:

```bash
poetry run task run
```

Fast Mocker will now be running on `localhost:8000` 🌐. You can access the API endpoints at `localhost:8000/{endpoint_path}`.

## YAML Configuration Files 📄

Before testing the API, you need to create your YAML configuration files in the `/mocks` folder. The YAML files should follow the same structure as the example files: `/mocks/animals.example.yml` and `/mocks/users.example.yml`.

### Example YAML Configuration ✏️

Here's an example of the YAML configuration format:

```yaml
Animals:
  GetAnimals:
    path: /animals
    method: get
    response:
      media_type: application/json
      status_code: 200
      content: Hello World

  PostAnimals:
    path: /animals
    method: post
    response:
      media_type: application/json
      status_code: 201
```

### Information ℹ️

- `Animals`: Entity (replace with your desired entity name).
- `[GetAnimals, PostAnimals]`: Templates (replace with your desired endpoint names).
- `path`: The endpoint that can be accessed with `localhost:8000/path`.
- `method`: The HTTP method to use when making a request to the path.
- `response`: The response that will be returned when calling the endpoint.
  - `media_type`: The type of the response.
  - `status_code`: The HTTP status code of the response.

## Testing with cURL 🧪

After configuring the YAML files, you can test the API using cURL. For example:

```bash
curl -X GET http://localhost:8000/animals
```

## Conclusion 🎉

You've now successfully installed, run, and tested Fast Mocker! Feel free to explore the project, create more YAML configurations, and simulate various API responses.

If you have any questions or encounter any issues, don't hesitate to reach out for help. Happy mocking! 😄🚀

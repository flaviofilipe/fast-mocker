# Fast Mocker 🚀

---

**Documentation**: <a href="https://fast-mocker.readthedocs.io/" target="_blank">https://fast-mocker.readthedocs.io/</a>

**Source Code**: <a href="https://github.com/flaviofilipe/fast-mocker" target="_blank">https://github.com/flaviofilipe/fast-mocker</a>

---

## Description 📝
Fast Mocker is a project developed in Python 3.11 using FastAPI. It serves as a tool to simulate a REST API by returning responses based on YAML files located in the /mocks directory. The project includes two example files: users.yml and animals.yml. 🐍✨

## Installation 🛠️
To install and set up the Fast Mocker project, follow the steps below:

### Prerequisites 📋
- Python 3.11
- Poetry 🎶

### Steps 🚀
1. Clone the repository from Github:
   ```
   git clone https://github.com/flaviofilipe/FastMocker.git
   ```

2. Change into the project directory:
   ```
   cd FastMocker
   ```

3. Install the project dependencies using Poetry:
   ```
   poetry install
   ```

## Developing 🚀
Follow the commands below to execute different tasks of the Fast Mocker application:

### Execute the application ▶️
```
poetry run task run
```

### Run tests 🧪
```
poetry run task test
```

### Validate the code (linting) ✅
```
poetry run task lint
```

### Automatically fix linting issues ✨
```
poetry run task fix_lint
```

### Generate coverage report 📊
```
poetry run task post_test
```

## Contributing 🤝
If you would like to contribute to Fast Mocker, follow the steps below:

1. Fork the repository on Github.

2. Clone your forked repository:
   ```
   git clone https://github.com/flaviofilipe/FastMocker.git
   ```

3. Create a new branch for your changes:
   ```
   git checkout -b feature/your-feature
   ```

4. Make the necessary changes and commit them:
   ```
   git add .
   git commit -m "Add your commit message here"
   ```

5. Push your changes to your Github repository:
   ```
   git push origin feature/your-feature
   ```

6. Create a pull request on the original repository to propose your changes.

## License 📜
This project is licensed under the [MIT License](LICENSE).

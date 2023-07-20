# Usage
## 📝 Creating YAML Configuration Files and Testing with Fast Mocker 🧪

Fast Mocker makes it a breeze to create and test YAML configuration files for your simulated API responses. This guide will walk you through the process of crafting these files and testing them with Fast Mocker.
Sure! Let's update the description for the `content` field in the YAML configuration:

## Step 1: Creating YAML Configuration Files 📄

To start, head to the `/mocks` folder in your Fast Mocker project. This folder is where you'll create your YAML configuration files, defining the API responses you want to simulate. Follow the format shown in the example files to ensure a smooth and consistent experience.

### YAML Configuration Format 🖊️

```yaml
EntityName:
  EndpointTemplate:
    path: /endpoint-path
    method: http-method
    response:
      media_type: response-media-type
      status_code: http-status-code
      content: response-content
```

- `EntityName`: Replace this with the name of your entity, such as "Animals" or "Users."

- `EndpointTemplate`: Choose a template name for your endpoint, e.g., "GetAnimals" or "PostUsers." These templates will be used to define different API endpoints.

- `path`: Set the endpoint path that can be accessed via `localhost:8000/path`.

- `method`: Define the HTTP method to use when making a request to the specified path (e.g., "get," "post," "put," etc.).

- `response`: Specify the API response for this endpoint.
  - `media_type`: Set the media type of the response, such as "application/json" or "text/plain."
  - `status_code`: Choose the desired HTTP status code for the response (e.g., 200, 404, 500, etc.).

- `content`: Customize the content of the response in JSON format or as a plain text message. For JSON data, use the following format:

```yaml
content:
  message: Hello User
  name: Flávio Filipe
  age: 26
```

You can include any relevant data for your API response within the `content` field.

## Step 2: Testing YAML Configurations with Fast Mocker 🚀

After creating your YAML configuration files, you're ready to test them with Fast Mocker. With the project up and running on `localhost:8000`, you can use various HTTP clients to interact with your API and validate the responses.

### Example Testing with cURL 🧪

Let's test an example endpoint using cURL:

```bash
curl -X GET http://localhost:8000/animals
```

Fast Mocker will respond with the specified API response defined in your YAML configuration file.

## Step 3: Experiment and Refine 🧪🔧

Fast Mocker gives you the flexibility to simulate various API scenarios. Feel free to experiment by modifying the YAML configurations. Simulate success, errors, delays, or any other situation you need to test your application thoroughly.

## Join the Fast Mocker Community 🤝

The Fast Mocker community is always here to help and support you in your testing endeavors. Share your experiences, ask questions, and contribute your insights to make Fast Mocker even better!

With Fast Mocker, creating and testing YAML configurations is a delightful and efficient process. So, dive in, create your API simulations, and test with ease using Fast Mocker! 🌟

If you have any questions or need assistance, don't hesitate to reach out. Happy mocking and testing! 😄🚀

I've updated the `content` description to include an example of returning JSON data with multiple fields. This will allow users to understand how to structure their JSON responses in the YAML configuration file. Let me know if there's anything else you'd like to add or modify!

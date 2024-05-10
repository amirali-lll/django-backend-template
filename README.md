# Template from the full service project template
This project is configuration of django web app with django-rest-framework and django-rest-auth for user authentication. It also includes a docker-compose file for running the project in a containerized environment.
and also have configurations for the following:
- django
- django-rest-framework
- django-rest-auth with JWT authentication
- django-cors-headers 
    > **Information:** I have added the custom middleware to handle this properly
- django-environ
- swagger for API documentation
- custom auth user model
    For this project, I have customized the user model to include the following fields:
    - phone number
    - unique email
    - birth date
    - gender
    > **Information:** You can customize the user model as per your requirements

### How to use the template
#### Backend
- Clone the project
    > **Note:** You can clone the project using the following command:
    ```bash
    git clone https://github.com/amirali-lll/django-backend-template.git
    ```

- Change the name of the project
    > **Note:** For changing project name search the "project_name" and "PROJECT_NAME" in the project and replace it with your project name, also change the name of project_name directory to your project name
    
    > **information:** you can use the tools like vs-code search tool to search and replace the project name


### How to run the project
- Clone the project
    > **Note:** You can clone the project using the following command:
    ```bash
    git clone https://github.com/amirali-lll/django-backend-template.git
    ```
#### Run backend
- Change the directory
    > **Note:** You can change the directory using the following command:
    ```bash
    cd django-backend-template/backend
    ```
- Create a virtual environment
    > **Note:** You can create a virtual environment using the following command:
    ```bash
    python -m venv venv
    ```
- Start the virtual environment
    > **Note:** You can start the virtual environment using the following command:
    ```bash
    source venv/bin/activate
    ```
- Install the requirements
    > **Note:** You can install the requirements using the following command:
    ```bash
    pip install -r requirements.txt
    ```
- Create a `.env` file in the near the `settings.py` file and add the following configurations:
    ```env
    SECRET_KEY='YOUR_SECRET_KEY'
    DB_NAME=YOUR_DB_NAME
    DB_USER=YOUR_DB_USER
    DB_PASSWORD=YOUR_DB_PASSWORD
    DB_HOST=YOUR_DB_HOST_ADDRESS
    DB_PORT=YOUR_DB_PORT
    DB_ENGINE=django.db.backends.postgresql_psycopg2 # You can change this as per your database this is for postgresql
    ```
- Run the migrations
    > **Note:** You can run the migrations using the following command:
    ```bash
    python manage.py migrate
    ```

- Create a superuser
    > **Note:** You can create a superuser using the following command:
    ```bash
    python manage.py createsuperuser
    ```

- Run the server
    > **Note:** You can run the server using the following command:
    ```bash
    python manage.py runserver
    ```
    > **Information:** You can access the server at `http://localhost:8000`






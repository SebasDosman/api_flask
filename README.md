# Configuration:

# Creating the Database:

1. Define the FLASK_APP Environment Variable:

    - For Unix/Linux/macOS Systems:
        ```bash
        export FLASK_APP=main
        ```
    - For Windows Systems (CMD):
        ```bash
        set FLASK_APP=main
        ```     

2. Required Libraries:

    ```bash
    virtualenv env
    cd env/Scripts
    activate
    cd ../..
    pip install -r requirements.txt
    ```

3-1. Import and Execute the Migration Script:

   ```bash
   flask shell
   from models import CheckList
   from config import db
   db.create_all()
   ```

   If you wish to make changes, you can drop all tables and execute again:

   ```python
   db.drop_all()
   db.create_all()
   ```

   However, please note that this action will delete all tables. Therefore, it's recommended to work with Flask-Migrate for more controlled migrations. You can find detailed information [here].(https://flask-migrate.readthedocs.io/en/latest/index.html).

3-2. Install Flask-Migrate and Execute the Commands:

    - Initialize Migrations:
        ```bash
        flask db init
        ```

    - Create a New Migration (this will generate a file with SQL instructions to apply the changes):
        ```bash
        flask db migrate -m "First migration"
        ```

    - Apply the Migration to the Database:
        ```bash
        flask db upgrade
        ```

4. Running the Project:

    ```bash
    python main.py
    ```
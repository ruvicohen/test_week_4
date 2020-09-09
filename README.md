# wwii missions

This Flask application allows users to get targets from wwii missions.

## Setup

1. Clone the repository:
   ```
   https://github.com/ruvicohen/test_week_4.git
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask toolz pytest sqlalchemy returns
   ```


4. Collect initial data:
   ```
   make sure to run the seed()
   ```

5. Run the application:
   ```
   python run.py
   ```

The application should now be running on your localhost.

## Running Tests

To run the tests, use the following command:
```
pytest
```

## API Endpoints

- GET `/api/targets Get targets 
- GET `/api/target/<target_id>`: Get details of a specific target

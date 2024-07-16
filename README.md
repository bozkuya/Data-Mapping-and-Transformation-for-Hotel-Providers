# Data Mapping and Transformation for Hotel Providers

## Overview

This project is a Data Migration System designed to integrate hotel data from multiple providers into a unified structure. The system reads raw data in JSON format, processes it, and uploads it to a relational database for further analysis. The system is implemented using Object-Oriented Programming (OOP) principles to create modular, reusable components.


## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd data_migration_system
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```


## Usage

1. **Prepare your database**:
    - Ensure you have a PostgreSQL database set up.
    - Update the database connection details in `main.py`.

2. **Run the main script**:
    ```sh
    python main.py
    ```

3. **Run tests**:
    ```sh
    python -m unittest discover -s tests
    ```

## File Descriptions

- **README.md**: This file. Provides an overview of the project and setup instructions.
  - **classes.py**: Defines the `Category`, `Chain`, and `Hotel` classes.
  - **data_migration.py**: Contains the function `parse_data` to read and process JSON data.
  - **database.py**: Contains the function `upload_to_db` to insert processed data into the database.
  - **error_handling.py**: Contains error handling logic for the data parsing process.
- **tests/**: Contains unit tests for the project.
  - **test_data_migration.py**: Tests the data migration functions.
  - **test_classes.py**: Tests the class definitions.
  - **test_database.py**: Tests the database functions.
- **example_hotel_data.json**: Example JSON data file for testing.
- **main.py**: Main script to run the data migration process.

## Implementation Details

### Class Definitions

- `Category`: Represents a hotel category.
- `Chain`: Represents a hotel chain.
- `Hotel`: Represents a hotel property.

### Data Parsing and Transformation

The `parse_data` function reads JSON data and maps it to the defined classes. It also links hotels to their respective categories and chains.

### Database Integration

The `upload_to_db` function uploads the parsed data to a relational database (PostgreSQL).

### Error Handling

Error handling mechanisms are implemented to address issues such as missing or invalid data.


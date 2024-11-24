# AirBnB Clone - The Console

## Project Description
The '0x00. AirBnB clone - The console' project is the first step in building a full web application that simulates the functionality of the AirBnB platform. This project is part of the SE Foundations program and focuses on creating a command-line interpreter to manage the application's data model.

The console serves as the backbone of the entire project and provides a foundation for future modules that include a web framework, database management, API development, and user interface integration. The command interpreter is written in Python, leveraging object-oriented programming (OOP) concepts to create an extensible and modular system.

## Key Features
- **Interactive Command Line Interface (CLI)**: The console allows for the creation, retrieval, updating, and deletion of various objects such as users, places, and amenities.
- **Serialization/Deserialization**: Object data is stored persistently using JSON, allowing for easy retrieval and manipulation.
- **Extensible Models**: Includes models for `BaseModel`, `User`, `Place`, `State`, `City`, `Amenity`, and `Review`, all inheriting from the `BaseModel` class.
- **Custom Commands**: The interpreter includes commands like `create`, `show`, `destroy`, `all`, and `update` to manage objects.
- **File Storage Engine**: Handles the serialization of object data to a JSON file and the deserialization of data back into Python objects.

## Technologies Used
- **Programming Language**: Python 3
- **Framework**: cmd module for command-line interface
- **File Format**: JSON for object storage
- **Testing Framework**: unittest for comprehensive test coverage

## How to Run
The console can be started in interactive mode by running:
```bash
$ ./console.py
```
Or in non-interactive mode using a command:
```
$ echo "create BaseModel" | ./console.py
```

## Usage Examples
- Create a new object:
```
(hbnb) create BaseModel
```
- Show an object:
```
(hbnb) show BaseModel <object_id>
```
- Update an attribute:
```
(hbnb) update BaseModel <object_id> <attribute_name> "<attribute_value>"
```

## Stracture
```
AirBnB_clone/                   # Root directory of the project
├── AUTHORS                     # Task 0: Contains the list of contributors
├── README.md                   # Task 0: Provides a description of the project
├── console.py                  # Task 6, 7, 10-16: Command interpreter with updates for advanced commands
├── Makefile                    # Contains commands for running tests, lint checks, and the console
├── models/                     # Directory for all model files
│   ├── __init__.py             # Task 5: Initializes the models package
│   ├── base_model.py           # Tasks 3, 4, 5: Defines the BaseModel class
│   ├── user.py                 # Task 8: Defines the User class
│   ├── state.py                # Task 9: Defines the State class
│   ├── city.py                 # Task 9: Defines the City class
│   ├── amenity.py              # Task 9: Defines the Amenity class
│   ├── place.py                # Task 9: Defines the Place class
│   ├── review.py               # Task 9: Defines the Review class
│   └── engine/                 # Directory for storage engine
│       ├── __init__.py         # Task 5: Initializes the engine package
│       └── file_storage.py     # Task 5, advanced tasks: Implements the FileStorage class with reload and save
└── tests/                      # Directory for all test files
    ├── __init__.py             # Task 2: Initializes the tests package
    ├── test_console.py         # Task 17: Unit tests for console commands (including advanced features)
    ├── test_models/            # Tests for model classes
    │   ├── __init__.py         # Task 2: Initializes test_models package
    │   ├── test_base_model.py  # Task 2: Unit tests for BaseModel
    │   ├── test_user.py        # Task 2: Unit tests for User
    │   ├── test_state.py       # Task 2: Unit tests for State
    │   ├── test_city.py        # Task 2: Unit tests for City
    │   ├── test_amenity.py     # Task 2: Unit tests for Amenity
    │   ├── test_place.py       # Task 2: Unit tests for Place
    │   └── test_review.py      # Task 2: Unit tests for Review
    └── test_engine/            # Tests for storage engine
        ├── __init__.py         # Task 2: Initializes test_engine package
        └── test_file_storage.py# Task 2: Unit tests for FileStorage class (including advanced persistence features)
└── web_static/
    ├── 0-index.html
    ├── 1-index.html
    ├── 2-index.html
    ├── 3-index.html
    ├── 4-index.html
    ├── 5-index.html
    ├── 6-index.html
    ├── 7-index.html
    ├── 8-index.html
    ├── styles/
    │   ├── 2-common.css
    │   ├── 2-header.css
    │   ├── 2-footer.css
    │   ├── 3-common.css
    │   ├── 3-header.css
    │   ├── 3-footer.css
    │   ├── 4-common.css
    │   ├── 4-filters.css
    │   ├── 5-filters.css
    │   ├── 6-filters.css
    │   ├── 7-places.css
    │   ├── 8-places.css
    └── images/

```

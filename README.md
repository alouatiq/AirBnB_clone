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
AirBnB_clone/
├── AUTHORS
├── README.md
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
└── tests/
    ├── __init__.py
    ├── test_models/
    │   ├── __init__.py
    │   ├── test_base_model.py
    │   ├── test_user.py
    │   ├── test_state.py
    │   ├── test_city.py
    │   ├── test_amenity.py
    │   ├── test_place.py
    │   └── test_review.py
    └── test_engine/
        ├── __init__.py
        └── test_file_storage.py
```

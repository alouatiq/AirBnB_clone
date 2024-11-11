# Makefile for AirBnB Clone - The Console

# Variables
PYTHON      = python3
PYCODESTYLE = pycodestyle
TEST_DIR    = tests
CONSOLE     = console.py

.PHONY: all test style run console clean help

# Default target
all: test style

# Run unit tests
test:
	@echo "Running unit tests..."
	@$(PYTHON) -m unittest discover $(TEST_DIR)

# Check code style
style:
	@echo "Checking code style with pycodestyle..."
	@$(PYCODESTYLE) models/*.py
	@$(PYCODESTYLE) models/engine/*.py
	@$(PYCODESTYLE) $(CONSOLE)
	@$(PYCODESTYLE) tests/*.py
	@$(PYCODESTYLE) tests/test_models/*.py
	@$(PYCODESTYLE) tests/test_engine/*.py

# Run the console in interactive mode
console:
	@echo "Starting the console in interactive mode..."
	@./$(CONSOLE)

# Run the console in non-interactive mode with a command
run:
	@read -p "Enter command to run: " cmd; \
	echo $$cmd | ./$(CONSOLE)

# Clean up generated files
clean:
	@echo "Cleaning up..."
	@rm -f file.json
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +

# Display help information
help:
	@echo "Makefile for AirBnB Clone - The Console"
	@echo ""
	@echo "Usage:"
	@echo "  make            - Runs tests and checks code style"
	@echo "  make test       - Runs unit tests"
	@echo "  make style      - Checks code style with pycodestyle"
	@echo "  make console    - Runs the console in interactive mode"
	@echo "  make run        - Runs a command in non-interactive mode"
	@echo "  make clean      - Cleans up generated files"
	@echo "  make help       - Displays this help message"

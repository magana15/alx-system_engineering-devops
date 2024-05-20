# TODO List Exporter

This project retrieves and exports the TODO list progress for employees using the JSONPlaceholder REST API. The data can be exported to both CSV and JSON formats.

## Requirements

- Python 3.8.5 or higher
- Requests library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/todo-list-exporter.git
    cd todo-list-exporter
    ```

2. **Install the necessary dependencies:**

    You can install the required libraries using `pip`:

    ```sh
    pip install requests
    ```

## Usage

The script supports three main functionalities:
1. Exporting a single employee's TODO list to a CSV file.
2. Exporting a single employee's TODO list to a JSON file.
3. Exporting all employees' TODO lists to a single JSON file.

### Export Single Employee's TODO List to CSV

To export the TODO list data for a specific employee to a CSV file, use the following command:

```sh
./script.py <employee_id> --csv
This will create a file named <employee_id>.csv with the tasks data for the specified employee.

Export Single Employee's TODO List to JSON

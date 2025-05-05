from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Route to get all items
@app.route('/items/<state>/<city>', methods=['GET'])
def get_items(state, city): 
    
    result = process_csv_by_columns("result.csv", [0,1], [state, city])
    
    if result is None:
        return jsonify({})
    return jsonify({'state': result[0], 'city': result[1], "county": result[2], "median_value": result[3], "median_tax": result[4]})

@app.route('/cities/<state>', methods=['GET'])
def get_cities(state):
    result =process_csv_by_columns("result.csv", [0], [state], return_all=True)
    return {"state": result
    




def process_csv_by_columns(filename, column_indices, target_values, return_all:False):
    """
    Processes a CSV file line by line, filtering based on multiple columns.

    Args:
        filename (str): The name of the CSV file.
        column_indices (list): A list of column indices to check (0-based).
        target_values (list): A list of corresponding target values for each column.
        action (function): A function to execute for matching rows, taking the row as input.
    """
    list = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            if all(row[i] == target_values[index] for index, i in enumerate(column_indices)):
                if not return_all:
                    return(row)
                else:
                    list.append(row[1])
        if return_all:
            return list
            


if __name__ == '__main__':
    app.run(debug=True)
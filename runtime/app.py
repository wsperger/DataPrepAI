from flask import Flask, request, jsonify
import importlib
import logging

app = Flask(__name__)

# Environment variable for environment setting (dev, test, prod)
# You can set this environment variable as needed for your deployment environment

# Define the directory where the scripts are located
SCRIPTS_DIRECTORY = "runtime/scripts"


@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.json
    if data and data.get('product') and data.get('action') and data.get('data'):
        product_name = data['product']
        action = data['action']
        data_payload = data['data']
        try:
            logging.info(f"Attempting to import module for product: {product_name}")
            product_module = importlib.import_module(f"api_products.{product_name}.{product_name}")
        except ModuleNotFoundError as mnfe:
            logging.error(f"Product '{product_name}' not found: {mnfe}")
            return jsonify({"status": "error", "message": f"Product '{product_name}' not found."}), 404

        # Ensure the action corresponds to an available function within the module
        if not hasattr(product_module, action):
            logging.error(f"Action '{action}' not available for product '{product_name}'.")
            return jsonify({"status": "error", "message": f"Action '{action}' not available for product '{product_name}'."}), 400

        # Execute the action function with the provided data
        try:
            action_function = getattr(product_module, action)
            logging.info(f"Executing action '{action}' for product '{product_name}'.")
            result = action_function(data_payload)
            logging.info(f"Action '{action}' for product '{product_name}' executed successfully. Result: {result}")
            return jsonify({"status": "success", "message": f"Action '{action}' executed successfully.", "result": result}), 200
        except Exception as e:
            logging.error(f"Error executing action '{action}' for product '{product_name}': {str(e)}")
            return jsonify({"status": "error", "message": f"Failed to execute action '{action}' for product '{product_name}'."}), 500
    else:
        return jsonify({"status": "error", "message": "Invalid request. 'product', 'action', or 'data' is missing."}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

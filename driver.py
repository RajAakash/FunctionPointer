import argparse
import sys
import importlib
import yaml


# def run_custom_config(config, task_name):
#     # Define the logic for running a custom configuration
#     # You can customize this function for your specific use case
#     print(
#         f"Running custom configuration for {task_name} with config: {config}")


# def handle_custom_config(custom_config_dict, all_configs):
#     # Define a custom configuration dictionary
#     custom_options = {
#         # Add your custom options here
#         # 'custom_option_1': 'value1',
#         # 'custom_option_2': 'value2'
#         2
#     }

#     # Begin iterating over each custom task
#     custom_tasks = custom_config_dict['custom_tasks']
#     custom_data_loaders = {}

#     for task in custom_tasks:
#         print("===========================")
#         print(f"Custom Task: {task}")
#         print("===========================")

#         # Check if the task is for a specific application's config or a function
#         if '.' not in task:
#             # We let this config run and save the data_loader
#             app_config = all_configs.get(task, {})
#             app_config.update(custom_options)
#             custom_data_loaders[task] = run_custom_config(app_config, task)
#         else:
#             # Otherwise, we have a function to call
#             module_name, func_name = task.rsplit('.', 1)
#             print('I am here', module_name)
#             module = importlib.import_module(module_name)
#             func = getattr(module, func_name)
#             # We provide all data loaders and the custom config for this task
#             func(custom_options)


def main():

    # Read the function name from the configuration file
    with open('config.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    function_name = config.get('function_to_call')
    print(function_name)
    # Split the function name to get the module and function names
    module_name, func_name = function_name.rsplit('.', 1)

    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get the function reference using getattr
    func = getattr(module, func_name)

    # Call the function with arguments
    result = func(10, 5)
    print("Result:", result)


if __name__ == "__main__":
    main()

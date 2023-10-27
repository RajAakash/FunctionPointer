import argparse
import sys
import importlib


def run_custom_config(config, task_name):
    # Define the logic for running a custom configuration
    # You can customize this function for your specific use case
    print(
        f"Running custom configuration for {task_name} with config: {config}")
    # Add your logic here


def handle_custom_config(custom_config_dict, all_configs):
    # Define a custom configuration dictionary
    custom_options = {
        # Add your custom options here
        # 'custom_option_1': 'value1',
        # 'custom_option_2': 'value2'
        2
    }

    # Begin iterating over each custom task
    custom_tasks = custom_config_dict['custom_tasks']
    custom_data_loaders = {}

    for task in custom_tasks:
        print("===========================")
        print(f"Custom Task: {task}")
        print("===========================")

        # Check if the task is for a specific application's config or a function
        if '.' not in task:
            # We let this config run and save the data_loader
            app_config = all_configs.get(task, {})
            app_config.update(custom_options)
            custom_data_loaders[task] = run_custom_config(app_config, task)
        else:
            # Otherwise, we have a function to call
            module_name, func_name = task.rsplit('.', 1)
            print('I am here', module_name)
            module = importlib.import_module(module_name)
            func = getattr(module, func_name)
            # We provide all data loaders and the custom config for this task
            func(custom_options)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str,
                        help='Keep config file by --config')
    args = parser.parse_args()
    print(args.config, type(args.config))
    # print(sys.argv[1]) --config
    if args.config:
        print(f'{args.config} is specified')
        custom_config = {
            'custom_tasks': [
                'task1',
                'task2',
                'math.exp'
            ]
        }
        all_configs = {
            'task1': {
                # Configuration options for 'task1'
                'option1': 'value1',
                'option2': 'value2',
                # Add any other task-specific configuration options
            },
            'task2': {
                # Configuration options for 'task2'
                'param1': 'param_value1',
                'param2': 'param_value2',
                # Add any other task-specific configuration options
            }
        }
        handle_custom_config(custom_config, all_configs)
    else:
        print('Specify --config')


if __name__ == "__main__":
    main()

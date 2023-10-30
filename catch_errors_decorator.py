
def catch_errors(func):
    def wrapper_catch_errors(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {e}")
    return wrapper_catch_errors


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})

# some_function_with_risky_operation({'key': 'bar'})


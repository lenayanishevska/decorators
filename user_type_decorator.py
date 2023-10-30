
def is_admin(func):
    def wrapper_is_admin(*args, **kwargs):
        if kwargs.get('user_type') == 'admin':
            return func(*args, **kwargs)
        else:
            raise ValueError("Permission denied!")
    return wrapper_is_admin
@is_admin
def show_customer_receipt(user_type: str):
    print(f'Your role ({user_type}) allows you to see this information')


try:
    # show_customer_receipt(user_type='user')
    show_customer_receipt(user_type='admin')
except ValueError as e:
    print(f"Error: {e}")


#!/usr/bin/python3
def safe_print_division(a, b):
    result1 = None
    try:
        result1 = a / b
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(result1))
        return result1

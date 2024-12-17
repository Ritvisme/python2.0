# try:
#     a=b;
# except NameError as ex:
#     print("NameError: ", ex);

# print("enter a number");
# try:
#     num1=int(input());
#     num2=int(input());
#     result=num1/num2;
#     print (result);
# except ZeroDivisionError as ex:
#     print("ZeroDivisionError: ", ex);
# except Exception as Z:
#     print("Exception: ", Z);
# finally:
#     print("finally block is executed");

# try:
#     file=open("data.txt", "r");
#     content=file.read();
#     print(content);
# except FileNotFoundError as ex:
#     print("FileNotFoundError: ", ex);
# finally:
#    if 'file' in locals() and not file.closed():
#     file.close() ;
#     print("finally block is executed");

def get_value_from_dict(data_dict, key):
    try:
        return data_dict[key]
    except KeyError:
        print(f"KeyError: '{key}' not found in the dictionary.")
    except ValueError:
        print("ValueError occurred.")
    finally:
        print("Lookup attempt complete.")

# Example usage
data = {"name": "Alice", "age": 25}

print(get_value_from_dict(data, "name"))  # Output: Alice
print(get_value_from_dict(data, "city"))  # Output: KeyError message + None
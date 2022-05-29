# Casting Tipe Data
# Merubah tipe data

# FROM INTEGER
data_int = 1;

# Casting
data_float = float(data_int); # Cast to float
data_str = str(data_int)    # Cast to str (string)
data_bool = bool(data_int)  # Cast to bool (boolean)

print("\n<-- INT --> ")
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool)) # akan false jika int = 0


# FROM FLOAT
data_float = 2.5;

# Casting
data_int = int(data_float); # Cast to int (integer)
data_str = str(data_float)    # Cast to str (string)
data_bool = bool(data_float)  # Cast to bool (boolean)

print("\n<-- FLOAT --> ")
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool))


# FROM STR (STRING)
data_str = "2";

# Casting
data_int = int(data_str); # Cast to int (integer)
data_float = float(data_str)    # Cast to str (string)
data_bool = bool(data_str)  # Cast to bool (boolean)

print("\n<-- STR --> ")
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool, "type = ", type(data_bool))


# FROM BOOL (BOOLEAN)
data_bool = False

# Casting
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)

print("\n<-- BOOL -->")
print("data = ", data_bool, "type = ", type(data_bool))
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))

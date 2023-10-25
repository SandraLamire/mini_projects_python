
# EXCEPTIONS - cf W3C doc

# print(x)
# NameError: name 'x' is not defined
try:
    print(x)
except:
    print('There is an error')
# There is an error


try:
    print(x)
except NameError:
    print('NameError means something is probably undefined.')
# NameError means something is probably undefined.

x = 2
try:
    print(x / 0)
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error")
# Please do not divide by zero
# I'm going to print with or without an error (finally is always print)

x = 2
try:
    if not type(x) is str:
        # use python error
        raise TypeError("Only strings are allowed.")
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error")
# Only strings are allowed.
# I'm going to print with or without an error

##############################################

# PERSONALIZED EXCEPTIONS

class JustNotCoolError(Exception):
    pass

x = 2
try:
    # raise Exception("I'm a custom exception!")
    raise JustNotCoolError("This just isn't cool, man!")
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error")
# This just isn't cool, man!
# I'm going to print with or without an error
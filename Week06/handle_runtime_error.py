# def div(a, b):
#     if b == 0:
#         return 'Error on b value!'
#     else:
#         return a / b

# print(div(2,0))
# print(div('hamid',3))

# def div2(a, b):
#     try:
#         return a / b
#     except Exception as e:
#         return e

# print(div2('hamid',0))

def div2(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Division by zero is not available!'
    except TypeError:
        return 'Type Error found!'
    except:
        return 'General error.'

print(div2('hamid',0))
# CUSTOM Exception design


class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    a = int(input('Enter a number:'))
    if a <= 0:
        raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received Error:", ae.data)
except Exception as e:
    print(e)
finally:
    print('Finally')

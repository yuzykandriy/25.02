result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a should be greater than or equal to b")
        if b == 0:
            raise ZeroDivisionError("b should not be zero")
        if b > 100:
            raise IndexError("b should not be greater than 100")
        return a / b
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"Exception occurred: {type(e).__name__} - {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)


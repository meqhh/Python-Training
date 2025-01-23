class Math:

    def add(*args):
        if not args:
            return 0

        result = 0

        for i in args:
            result += i

        return result

    def minus(*args):
        if not args:
            return 0

        result = args[0]
        for i in args[1:]:
            result -= i

        return result

    def multiply(*args):
        if not args:
            return 0

        result = 0
        for i in args:
            result *= i

        result = int(result)

        return result

    def divide(*args):
        if not args:
            return 0

        result = 0

        for i in args:
            if i == 0:
                return 0
            else:
                result /= i

        return result

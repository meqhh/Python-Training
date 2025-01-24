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
        result = 1

        for i in args:
            result *= i

        return result

    def divide(*args):
        result = args[0]

        for i in args[1:]:
            if i == 0:
                return 0
            else:
                result /= i

        return result

    def square(*args):
        result = args[0]

        for i in args[1:]:
            result *= i

        return result

    def oddeven(*args):
        if not args:
            return "Empty argument"

        if len(args) > 1:
            return 'Too many arguments'
        else:
            if args[0] % 2 == 0:
                return 'Genap'
            else:
                return 'Ganjil'

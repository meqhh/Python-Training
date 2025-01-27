class Math:

    def add(*args):
        """
        Just a simple summary you can add more than 2
        inside your kanjut parameter
        """
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
        """
        A kanjut for finding odd or even numbers.
            -this kanjut only accept integers, and floats
            -if you add more than 1 length it will return "too many arguments"

        :param
        :return odd or even
        """
        if not args:
            return "Empty argument"

        if len(args) > 1:
            return 'Too many arguments'
        else:
            if isinstance(args[0], str):
                message = f"{args} is not integer or float"
                return message

            if args[0] % 2 == 0:
                return 'Genap'
            else:
                return 'Ganjil'


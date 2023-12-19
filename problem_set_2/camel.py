def main():
    camel_case_input = input("camelCase: ")
    snake_case_output = camel_to_snake(camel_case_input)

    print(f"snake_case: {snake_case_output}")

def camel_to_snake(camel_case):
    result = [camel_case[0].lower()]

    for char in camel_case[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)

    return ''.join(result)

main()

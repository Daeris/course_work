from utils import load_operations, display_operations

def main():
    operations = load_operations('operations.json')
    print(operations)  # Вывод всего содержимого
    display_operations(operations)


if __name__ == "__main__":
    main()


def sandwich_items(*items):
    print("\nPreparing your sandwich")
    for item in items:
        print(f"Adding {item} to your sandwich")

sandwich_items('celery', 'tomato', 'beef')
sandwich_items('cucumber', 'chicken')
sandwich_items('tuna')
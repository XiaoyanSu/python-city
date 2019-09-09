def draw_school(floors=0):
    """prints a school with specified # of floors
        Args:
            floors: integer representing the number of floors above ground level
    """
    #Sanitize Parameter
    if floors < 0:
        raise ValueError("number of floors cannot be negative")
    #Printing School
    print("  .  ")
    print(" / \\ ")
    print(" | | ")
    print("/   \\")
    for _ in range(floors):
        print("|   |")
    print("|___|")
    return

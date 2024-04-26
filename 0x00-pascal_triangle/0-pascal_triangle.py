def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0
    
    triangle = []  # Initialize the list to store the rows of Pascal's triangle
    
    for i in range(n):
        row = []  # Initialize a list for the current row
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  # The first and last elements in each row are 1
            else:
                # Other elements are the sum of the two elements directly above in the previous row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)  # Add the current row to the triangle list
    
    return triangle

# Test the function using the provided main script
def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))




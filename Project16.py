def square_ranges(start, end):
    squares = [num ** 2 for num in range(start, end + 1)]
    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
            
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")

square_ranges(1, 5)
start_row  = int(input("Enter start row: "))
start_column  = int(input("Enter start column: "))

finish_row = int(input("Enter finish row: "))
finish_column = int(input("Enter finish column: "))

if (start_row > 0 and start_row <= 8 
    and start_column > 0 and start_column <= 8
    and finish_row > 0 and finish_row <= 8 
    and finish_column > 0 and finish_column <= 8):
    
    if (abs(finish_row-start_row)==1 and abs(finish_column-start_column)==2
        or abs(finish_row-start_column)==2 and abs(finish_column-start_column)==1):
        answer = "Yes"
    else:
        answer = "No"

else:
    answer = "NOT CORRET DATA!"

print(answer)
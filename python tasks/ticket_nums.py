def is_happy(ticket_num):

    right_side = 0
    left_side = 0

    for i in range(len(ticket_num)):
        if i > 3:
            left_side += int(ticket_num[i])
        else:
            right_side += int(ticket_num[i])

    if left_side == right_side:
        print("Счастливый")
    else:
        print("Обычный")

def main():
    
    tickets = ["000000","000001","111111","090234","763196","123321"]
    for ticket in tickets:
        print (tiket)
        is_happy(ticket)

if __name__ == "__main__":
    main()
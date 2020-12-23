def UpdateMin(faulty_list):
    # Write your code here
    if faulty_list == None:
        return None
    pr = faulty_list
    head = faulty_list.next
    while head:
        if pr.data > head.data:
            head.data = (pr.data+head.next.data)//2
        pr = head
        head = head.next
    return faulty_list

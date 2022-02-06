def removeDuplicates(llist):
    head = None
    tail = None
    temp = llist.data

    while llist:
        if not head:
            head = llist
            tail = head
        elif temp == llist.data:
            if not llist.next:
                tail.next = None
        else:
            tail.next = llist
            tail = llist
            temp = tail.data

        llist = llist.next

    return head

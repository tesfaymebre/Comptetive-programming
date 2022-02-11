def has_cycle(head):
    visited = set()
    if not head:
        return 0

    while head.next:
        if head in visited:
            return 1

        visited.add(head)
        head = head.next

    return 0

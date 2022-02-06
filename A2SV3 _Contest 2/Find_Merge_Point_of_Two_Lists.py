def findMergeNode(head1, head2):
    seen = dict()
    p1 = head1
    p2 = head2

    while p1:
        seen[p1] = 1
        p1 = p1.next
    while p2:
        if p2 in seen:
            return p2.data
        p2 =p2.next
    return 0

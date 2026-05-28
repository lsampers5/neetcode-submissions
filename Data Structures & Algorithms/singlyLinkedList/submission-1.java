class LinkedList {
    private class Node {
        private int val;
        private Node next;

        public Node (int val) {
            this.next = null;
            this.val = val;
        }
    }
    private Node head;
    private Node tail;
    private int size;

    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public int get(int index) {
        if (index >= size || index < 0) { // make sure the index is good
            return -1;
        }
            Node current = head;
            for (int i = 0; i < index; i++) {
                current = current.next;
            }
                    return current.val;
        }

    public void insertHead(int val) {
        Node newNode = new Node(val); // [newNode -> 5 -> null]
        newNode.next = head; // [head -> 2 -> 3-> 4] makes it [newNode -> 5 -> 2 -> 3 -> 4] 
        head = newNode; //[head ->5 -> 2 ]
        if (tail == null) {
            tail = newNode;
        }
        size++;
    }

    public void insertTail(int val) {
        Node newNode = new Node(val); 
         if (tail == null) {
            head = tail = newNode;
         } else {
            tail.next = newNode;
            tail = newNode;
         }
         size++;
    }
    

    public boolean remove(int index) {
        // Check if valid index I think this also checks if the list is empty cause size should be a correct field
        if (index >= size || index < 0) {
            return false;
        }
        // Index 0 special because it is the first element in the list
        if (index == 0) {
            head = head.next;
            size--;
            return true;
        }
        Node current = head;

        for (int i = 0; i < index - 1; i++) { // Moving the pointer to be right before the element I want to remove
            current = current.next;
        }
        if (current.next == tail) {
            tail = current; //Little edge case protection if you want to remove the tail
        }
        current.next = current.next.next; // skips the element and removes cause nothing points to it anymore
        size--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> result = new ArrayList<>();
        Node current = head;
        while (current != null) {
            result.add(current.val);
            current = current.next;
        }
        return result;
    }
}

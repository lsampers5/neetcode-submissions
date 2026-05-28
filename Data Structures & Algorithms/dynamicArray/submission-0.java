class DynamicArray {
    private int size;
    private int capacity;
    private int[] arr;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.arr = new int[capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == capacity) { // Does it need to resize
            resize();
        }
        arr[size] = n; // fills in the next spot needed
        size++; // Updates size to stay consistent
    }

    public int popback() {
        //assume array is not empty
        int result = arr[size - 1];
        arr[size - 1] = 0;
        size--;
        return result;
    }

    private void resize() {
        capacity *= 2; 
        int[] newArr = new int[capacity];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}

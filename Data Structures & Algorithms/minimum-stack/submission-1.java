
class MinStack {
    class IntPrevMin {
        int index;
        int value;

        public IntPrevMin(int i, int v) {
            this.index = i;
            this.value = v;
        }
    }
    List<IntPrevMin> mins;
    List<Integer> list;
    int pointer;

    public MinStack() {
        this.list = new ArrayList<Integer>();
        this.mins = new ArrayList<IntPrevMin>();
        this.pointer = 0;
    }
    
    public void push(int val) {
        list.add(val);

        if (mins.size() == 0 || val < mins.get(mins.size() - 1).value) {
            mins.add(new IntPrevMin(pointer, val));
        }
        pointer++;
    }
    
    public void pop() {
        pointer--;
        if (pointer == mins.get(mins.size() - 1).index) {
            mins.remove(mins.size() - 1);
        } 
        list.remove(pointer);
    }
    
    public int top() {
        return list.get(pointer - 1);
    }
    
    public int getMin() {
        return mins.get(mins.size() - 1).value;
    }
}

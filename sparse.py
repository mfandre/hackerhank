
# importing the sys module
import sys

sys.setrecursionlimit(10**6)

class SparseArray:
    __items = {}

    def addItem(self, i, value):
        self.__items[i] = value

    def getItem(self, i):
        try:
            return self.__items[i]
        except KeyError:
            return None
    
    def __repr__(self) -> str:
        return str(self.__items)

class RangeDict(dict):
    # def range_intersection(self, *ranges):
    #     ranges = set(ranges)  # `range` is hashable so we can easily eliminate duplicates
    #     if not ranges: return
        
    #     shortest_range = min(ranges, key=len)  # we will iterate over one, so choose the shortest one
    #     ranges.remove(shortest_range)          # note: `range` has a length, so we can use `len`
        
    #     for i in shortest_range:
    #         if all(i in range_ for range_ in ranges): yield i  # Finally, `range` implements `__contains__`
    #                                                         # by checking if an iteger satisfies it's simple formula

    def is_overlapping(self, x, y):
        #if x.start == x.stop or y.start == y.stop:
        #    return False
        return x.start <= y.stop and y.start <= x.stop
    
    def overlap(self, x, y):
        if not self.is_overlapping(x, y):
            return []
        return list(range(max(x.start, y.start), min(x.stop, y.stop)+1))

    def __setitem__(self, __key, __value) -> None:
        for key in self:
            if self.is_overlapping(__key,key):
                #__key = rg2
                #  key = rg1
                #print(f"{__key} is overlapping {key}")
                print(self.overlap(__key, key))
                union = range(min(__key.start, key.start), max(__key.stop, key.stop))
                #print("=========>",union)
                self.update({union: __value})
                if union != key:
                    self.pop(key)
                return

        return super().__setitem__(__key, __value)

    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            for key in self:
                if self.is_overlapping(item,key):
                    return super().__getitem__(key)

            return super().__getitem__(item)

class SparseRanges:
    __items = {}

    def addItem(self, key:str, value):
        self.__items[key] = value

    def getItem(self, key):
        try:
            return self.__items[key]
        except KeyError:
            return None
    
    def __repr__(self) -> str:
        return str(self.__items)

class BSTNode:
    def __init__(self, val=None, index=None):
        self.left = None
        self.right = None
        self.val = val
        self.index = index

    def addItem(self, index, val):
        if self.index is None and index != None:
            self.val = val
            self.index = index
            return

        if self.index == index:
            return

        if index < self.index:
            if self.left:
                self.left.addItem(val, index)
                return
            self.left = BSTNode(val, index)
            return

        if self.right:
            self.right.addItem(val, index)
            return
        self.right = BSTNode(val, index)

    def exists(self, index):
        if index == self.index:
            return self

        if index < self.index:
            if self.left == None:
                return None
            return self.left.exists(index)

        if self.right == None:
            return None
        return self.right.exists(index)

    def getItem(self, index):
        if self.index is None:
            return None

        if index == self.index:
            return self

        if index < self.index:
            if self.left == None:
                return None
            return self.left.exists(index)

        if self.right == None:
            return None
        return self.right.exists(index)
    
    def set(self, val, index, new_val):
        if index == self.index:
            self.val = new_val
            return True

        if index < self.index:
            if self.left == None:
                return False
            return self.left.exists(index)

        if self.right == None:
            return False
        return self.right.exists(index)
    
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

def arrayManipulation1(n, queries):
    sparse_array = SparseArray()
    # Write your code here
    #print(queries)
    iteration = 0
    max = -999999999
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]

        for i in range(a,b+1):
            item_in_index_i = sparse_array.getItem(i)
            if item_in_index_i is not None:
                temp_sum = item_in_index_i+k
                sparse_array.addItem(i, temp_sum)
                if  temp_sum > max:
                    max = temp_sum
            else:
                sparse_array.addItem(i, k)
        iteration += 1
        print(f"it={iteration}")
    #print(sparse_array)
    return max

def arrayManipulation(n, queries):
    sparse_keys = RangeDict()
    # Write your code here
    #print(queries)
    iteration = 0
    max = -999999999
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]

        try:
            current_value = sparse_keys[range(a,b)]
            temp_sum = current_value + k
            sparse_keys[range(a,b)] = temp_sum
            if temp_sum > max:
                max = temp_sum
        except KeyError:
            sparse_keys[range(a,b)] = k

        iteration += 1
        print(f"it={iteration}")
    print(sparse_keys)
    return max

def main():
    n = 5
    queries = []#[[1, 2, 100], [2, 5, 100], [3, 4, 100]] # 200

    f = open("test_case2_sparse")
    line_number = 0
    for line in f:
        if line_number == 0:
            n = line.split(' ')[1]
            line_number += 1
            continue
    
        data = line.split(' ')
        temp_data = []
        for item in data:
            item = int(item.replace('\n',''))
            temp_data.append(item)
        queries.append(temp_data)
        line_number += 1
    #print(queries)
    print(arrayManipulation(n, queries)) # 2510535321

if __name__ == "__main__":
    main()
    

    # rd = RangeDict()
    # rd[range(0,5)] = 1
    # print(rd, "(0,5)")
    # rd[range(3,6)] = 0
    # print(rd, "(3,6)")
    # rd[range(4,10)] = 2
    # print(rd, "(4,10)")
    # rd[range(20,40)] = 0
    # print(rd, "(20,40)")
    # print(rd[range(60,89)])
    
    # tree = BSTNode()
    # tree.addItem(10,0)
    # tree.addItem(11,1)
    # tree.addItem(26,2)
    # tree.addItem(8,3)
    # tree.addItem(0,4)
    # tree.addItem(50,5)

    # print(tree.inorder([]))

    # index = 8
    # found = tree.getItem(index)
    # print(found)
    # if not found:
    #     print(index, "not found")
    # else:
    #     print(found.val)
    #     print(index, "found")


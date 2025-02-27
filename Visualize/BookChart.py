# thiết kê ý tưởng
# tính đường đi gần nhất
# giữa các điểm với nhau
# phải có các đường đi và khoảng cách giữa các điểm
# vấn đề là thuật toán thế nào
#  cho 4 điểm A,B,C,D
# một list các khoảng cách tới các điểm với nhau tương ứng
# Tập hợp thành một file có chứa dữ liệu của tên đường và khoảng cách
# không ăn trước khi ngủ, khong xem điện thoiaj trc khi ngủ, không uống cafein hay những chất gay kich hích, không nangawjnddaau frrc khi ngủ, đừng ép bản thân ngủ
# def dO

# code bào tán có n nam và n nữ cho vào 1 bàn tròn với một nam thì kế đó có 1 nữ hiện hết tất cả các cách xếp nam nữ vào
# dATA STRUTURES AND ALGORITHM


# linked list

class Node():
    def __init__(self,a_number):
        self.data= a_number
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None: # duyệt đi lên từ từ vì cuối node luôn luôn là None nếu là None thì dừng lại để thêm phần tử tiếp theo
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


def reverse(l):
    if l.head is None:
        return

    current_node = l.head
    prev_node = None

    while current_node is not None:
        # Track the next node
        next_node = current_node.next

        # Modify the current node
        current_node.next = prev_node

        # Update prev and current
        prev_node = current_node
        current_node = next_node

    l.head = prev_node


# Binary Tree
class binaryTree():
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def InOrder(temp):
        if (not temp):
            return
        InOrder(temp.left)
        print(temp.val,end = " ")
        InOrder(temp.right)
# function to insert element in binary tree
def insertTree(temp,key):
    if (not temp):
        root=binaryTree(key)
        return
    q=[]
    q.append(temp)
    while (len(q)):
        nums=q[0]
        q.pop(0)
        if (not nums.left):
            nums.left=binaryTree(key)
            break
        else:
            q.append(nums.left)

        if (not nums.right):
            nums.right = binaryTree(key)
            break
        else:
            q.append(nums.right)


def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


# function to delete element in binary tree
def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while (len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root







class Solution:
    def subArraySum(self, arr, n, s):
        # Write your code here
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            arr[0] = s
            return 1
        Index = 0
        nums = 0
        SumArr = 0
        while nums >= 0:
            SumArr += arr[nums]
            nums += 1
            if SumArr == s:
                return Index + 1, nums
            elif SumArr > s:
                SumArr -= arr[Index]
                Index += 1
                if SumArr == s:
                    return Index + 1, nums
            elif nums == n - 1:
                if (SumArr + arr[n - 1]) == s:
                    return Index + 1, nums + 1
                else:
                    return -1


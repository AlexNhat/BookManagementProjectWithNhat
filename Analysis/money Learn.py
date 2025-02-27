from collections import Counter

## MIN EDIT DISTANCE


def MinEditDistance(Str1,Str2):
    # hai tham số chứa giá trị của hai chuổi
    lenth1, lenth2=len(Str1),len(Str2)
    if lenth1==0:
        return lenth2
    if lenth2==0:
        return lenth1
    # Nếu chữ cái cuối của hai chuổi bằng nhau thì duyệt tiếp nhưng xóa đi phần chữ cái cuối cùng
    if Str1[lenth1-1]==Str2[lenth2-1]:
        return MinEditDistance(Str1[:lenth1-1],Str2[:lenth2-1])
    # Vf tạo ra ba đường đi trong các lưaj chọn
    # độ phức tạp của thuật toán là O(n**2) duyệt theo 3 con đường và thê là xong
    return 1+ min(MinEditDistance(Str1,Str2[:lenth2-1]), MinEditDistance(Str1[:lenth1-1],Str2)
                  ,MinEditDistance(Str1[:lenth1-1],Str2[:lenth2-1]))


# giải bài toán tìm số lớn nhất được tạo ra từ một dãy số
def MaxMergeElement(elementList):
    # elementList là một list chưa các số
    # StrList={}
    # for nums in range(len(elementList)):
    #     StrList[str(elementList[nums])]=nums
    # pivot=max(elementList)
    # lenth=len(pivot)
    # for k in range(lenth):
    #     # lúc này ta cần đổi chổ chúng với nhau trong dict thông qua thông số
    #
    pass
# print(MaxMergeElement([90,56,123,124]))











# Thuật toán sẽ như thế này lấy các số đầu tiên của con số có độ dài bằng nhau đem nó ra so sánh riêng
# ví dụ [96, 56, 923, 124] Nếu làm theo cách thông thường ta sẽ tổ hợp chúng lại với nhau sau đó tìm số lớn nhất
# Nhưng nếu làm vậy a sẽ làm cho nó tới taa n^2 và nó phải duyệt rất là lâu
# chúng ta sẽ dùng cách chia để trị ta sẽ chia ra số lớn và số bé như ví dụ trên sếp hai số
# ta sẽ so sánh từng đợt ví dụ lúc đầu so sánh số cuối thì ta được [96,56,124,123] so sánh số thứ 2 [96,56,124,923]
# Kiểm tra xem số nào không còn chia đc nữa thì lấy ra khỏi list sau đó thì tiếp tục [923,124]

# 9656124123

def largestNumber(array):
    #If there is only one element in the list, the element itself is the largest element.
    #Below if condition checks the same.
    if len(array)==1:
        return str(array[0])
    #Below lines are code are used to find the largest element possible.
    #First, we convert a list into a string array that is suitable for concatenation
    for i in range(len(array)):
        array[i]=str(array[i])
    print(array)
    # [54,546,548,60]=>['54','546','548','60']
    #Second, we find the largest element by swapping technique.
    for i in range(len(array)):
        for j in range(1+i,len(array)):
            if int(array[j]+array[i])>int(array[i]+array[j]):
                array[i],array[j]=array[j],array[i]
    #['60', '548', '546', '54']
    #Refer JOIN function in Python
    result=''.join(array)
    #Edge Case: If all elements are 0, answer must be 0
    if(result=='0'*len(result)):
        return '0'
    else:
        return result
arr = [90,56,123,124]
print(largestNumber(arr))

a='a23'
b='134'
if a+b>b+a:

    print(1)
else:
    print(2)


def fibonacci1(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def fibonacci2(n):
    if n==0:
        return 0
    current=1
    previous=0
    for nums in range(1,n):
        newelement=current+previous
        previous=current
        current=newelement

    return current



# Thuật toán là như thế này nhé
# Chúng ta sẽ kiểm tra từng phần tử sau đó kiếm vị trí nào chưa phần tử đầu tiên trong word nếu kiêm thấy nó ta
# sẽ bắt đầu duyệt các lận cận của nó trên dưới trái phải nếu cái nào đúng thì ta duyệt tiếp tục còn sai
# ta sẽ đi lại hướng khác
# Và khi duyệt không được lặp lại các chổ đã duyệt qua sai thì đi lai
# Và người ta sẽ dùng duyệt theo DFS để giải quyết bài toán này.


class Solution(object):
   def exist(self, board, word):
       # Lấy độ dài của hai chuổi mà làm
       # Nếu duyệt mà k có cái nào trùng với ký tự đầu tien của word thì trả về False
       # còn có Thì duyệt tiếp đến khi nào kiểm tra đầy đủ trả về True
      n =len(board)
      m = len(board[0])
      for i in range(n):
         for j in range(m):
            if word[0] == board[i][j]:
               if self.find(board,word,i,j):
                  return True
      return False

   # Hàm Tìm kiếm tất cả còn lại gồm 4 tham số là board ,word, dòng và cột và i mặt định bằng 0
   def find(self, board,word,row,col,i=0):
    # Nếu mà i dùng để kiểm tra đã đủ độ dài word để dừng nếu đủ thì cho nó trả về True
      if i== len(word):
         return True

    # Nếu kiểm tra độ dài dong lớn hơn hoặc bằng độ dài của board
    # hay dòng đó nhỏ hơn 0 hay cột lớn hơn độ dài của 1 dòng board
    # hay cột nhỏ hơn 0 hay word[i] khác với board[row][col] hiện tại thì trả về false
      if row>= len(board) or row <0 or col >=len(board[0]) \
              or col<0 or word[i]!=board[row][col]:

         return False
      board[row][col] = '*'
    # Không thì ta sẽ đệ quy tho 4 trường hợp bên phải bên trái bên trên và ở dưới để kiếm xem có đúng không
      res = self.find(board,word,row+1,col,i+1) or self.find(board,word,row-1,col,i+1) or \
            self.find(board,word,row,col+1,i+1) or self.find(board,word,row,col-1,i+1)
      # và cuối cùng sẽ là sẽ cho vị trí từ đó trong bảng bằng với
      board[row][col] = word[i] # Là k lập lại đường đi cũ
      return res
ob1 = Solution()
print(ob1.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))





# def edit_distance(str1, str2, a, b):
#     # a b là chiều dài chuổi
#     # Tạo ra ma trận để tính và +1 là vì so sánh với chữ khởi tạo là 0
#     string_matrix = [[0 for i in range(b + 1)] for i in range(a + 1)]
#     # Duyệt hai vòng lặp
#     for i in range(a + 1):
#         for j in range(b + 1):
#             # Khởi tạo các chi phí cơ sở với điểm bắt đầu
#             if i == 0:
#                 string_matrix[i][j] = j  # If first string is empty, insert all characters of second string into first.
#             elif j == 0:
#                 string_matrix[i][j] = i  # If second string is empty, remove all characters of first string.
#             # Nếu hai chữ cái phía trước i và j giống nhau thì thì phía sau chi phí cộng vào là 0 nên gán cho nó chi phí bằng cái trước
#             # đoạn này mang ý  nghĩa là k có sự thay thế
#             elif str1[i - 1] == str2[j - 1]:
#                 string_matrix[i][j] = string_matrix[i - 1][
#                     j - 1]
# # If last characters of two strings are same, nothing much to do. Ignore the last two characters and get the count of remaining strings.
#             # còn lại thì buộc phải có chuyển đổi hay insert hoặc delete
#             else:
#                 string_matrix[i][j] = 1 + min(string_matrix[i][j - 1],  # insert operation
#                                               string_matrix[i - 1][j],  # remove operation
#                                               string_matrix[i - 1][j - 1])  # replace operation
#     # cuối cùng trả về chi phí nhỏ nhất
#     return string_matrix[a][b]
#
#
# if __name__ == '__main__':
#     str1 = 'intention'
#     str2 = 'ecutention'
#     print('No. of Operations required :', edit_distance(str1, str2, len(str1), len(str2)))
#
#     str3 = 'Saturday'
#     str4 = 'Sunday'
#     print('No. of Operations required :', edit_distance(str3, str4, len(str3), len(str4)))



#Character Based Distance
# Hàm tồng quát
## Minimum edit distance
import numpy as np
  def Calculate_Minimum_edit_distance(source,target):
      n= len(source)
      m= len(target)
      MED_Matrix= np.zeros((n+1,m+1), dtype='int32')
      for i in range(1,n+1):
          MED_Matrix[i][0]=MED_Matrix[i-1][0]+del_cost
      for i in range(1,m+1):
          MED_Matrix[0][i]=MED_Matrix[0][i-1]+del_cost
      for i in range(1,n+1):
          for j in range(1,m+1):
              if(source[i-1]==target[j-1]):
                  MED_Matrix[i][j]=min([MED_Matrix[i-1][j]+del_cost,MED_Matrix[i-1][j-1]+0,MED_Matrix[i][j-1]+ins_cost])
              else:
                  MED_Matrix[i][j]=min([MED_Matrix[i-1][j]+del_cost,MED_Matrix[i-1][j-1]+sub_cost,MED_Matrix[i][j-1]+ins_cost])
      #print(np.matrix(MED_Matrix))
      #print(MED_Matrix[n][m])
      return MED_Matrix[n][m]




  #Thuật toán Byte pair encoding dùng để nén dữ liệu
  # Nó vừa đơn giản dữ liệu vừa khiến dữ liệu dễ dùng hơn nhưng câu hỏi đặt ra nó sẽ dùng chung duy nhất
  # các ký tự đã nén đại diện cho dữ liệu  bằng cách nào bây giờ là cần tìm hiểu cách thuật toán đếm của nó
  # hoạt đọng bằng cachsh nào

def BytePairEncoding(corpus, elements):
    Vocab=set()
    for k in range(1,elements):
        pass

















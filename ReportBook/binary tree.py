import math
import time

c=time.time()
def readFileTxtTolists(strPath):
    # biến f đang mở file txt để read
    f = open(strPath, "r")
    # khởi tạo 2 danh sách tạm để chút nữa chứa thông tin cần thiết
    list_vertices_temp = []
    list_faces_temp = []
    # duyệt từng dòng của biến f xem nó thuộc mô tả của Vertice hay Face
    for line in f:
        # nếu dòng đó bắt đầu bằng ký từ v nghĩa là đang mô tả Vertice
        if line[0] == 'v':
            # tạo biến đã loại bỏ ký tự xuống dòng \n ở cuối dòng bằng cách thay thế ký tự \n thành ký tự null
            removed_line = line.replace('\n','')
            # loại bỏ tiếp chữ v ở đầu dòng

            # tách nhỏ chuỗi còn lại dựa vào khoảng trống, lúc này ta sẽ có một mảng chứa tọa độ của đỉnh
            removed_line_array = removed_line.split(' ')
            # chuyển 3 ký tự của mảng đã tách ở trên sang dạng mảng số cho dễ tính toán sau này
            removed_line_array = [eval(removed_line_array[1]),eval(removed_line_array[2]),eval(removed_line_array[3])]
            # lúc này mọi công tác chuẩn bị đã xong, đưa biến cuối vào danh sách đỉnh đã chuẩn bị ở trước đó
            list_vertices_temp.append(removed_line_array)
            # lặp lại cho tới khi hết dòng có ký tự v ở đầu là ta đã có danh sách tọa độ các Vertices được lưu riêng
        # làm tương tự với các dòng có chữ f
        elif line[0] == 'f':
            removed_line = line.replace('\n','')

            removed_line_array = removed_line.split(' ')
            removed_line_array = [eval(removed_line_array[1]),eval(removed_line_array[2]),eval(removed_line_array[3])]
            list_faces_temp.append(removed_line_array)
            # lúc này danh sách sẽ chứa thứ tự Vertices để tạo ra một Face
    # hàm này trả về 2 danh sách, một là danh sách Vertices, một là danh sách Faces
    return list_vertices_temp,list_faces_temp


list_vertices,list_faces=readFileTxtTolists('testerror.obj')

begin=len(list_vertices)

# trả về khoảng cách giữa hai điểm
def DistanceTwopoint(x,y):
    return math.sqrt((x[2]-y[2])**2+(x[1]-y[1])**2+(x[0]-y[0])**2)


def calAreaTriEdge(v1,v2,v3):
    # tính khoảng cách giữa đỉnh 1 và 2 rồi lưu vào biến v1v2_distance
    v1v2_distance = DistanceTwopoint(v1,v2)
    # tính khoảng cách giữa đỉnh 2 và 3 rồi lưu vào biến v2v3_distance
    v2v3_distance = DistanceTwopoint(v2,v3)
    # tính khoảng cách giữa đỉnh 1 và 3 rồi lưu vào biến v1v3_distance
    v1v3_distance = DistanceTwopoint(v1,v3)
    # Tạo biến P tính chu vi của tam giác
    P = 0.5*(v1v2_distance+v2v3_distance+ v1v3_distance)
    # Tạo biến S chứa diện tích của tam giác dựa vào công thức tính P
    S =math.sqrt(P*(P-v1v2_distance)*(P-v2v3_distance)*(P-v1v3_distance))
    # hàm này trả về diện tích của tam giác cần tính
    return S


def calFaceAreas(list_vertices,list_faces):
    # khởi tạo một danh sách chứa diện tích cần tính
    list_facewithArea = []
    # duyệt từng Face trong danh sách Faces
    for i in range (len(list_faces)):
        # lấy tọa độ từng điểm trong từng face đang duyệt bởi vòng lặp for
        v1 = list_vertices[ list_faces[i][0]-1]
        v2 = list_vertices[ list_faces[i][1]-1]
        v3 = list_vertices[ list_faces[i][2]-1]

        S_Face = calAreaTriEdge(v1,v2,v3)
        # lưu kết quả diện tích kèm với thứ tự của Face để truy xuất sau này
        list_facewithArea.append([S_Face,i])
    # trả về thứ tự của Face kèm với diện tích của Face tương ứng
    return list_facewithArea

list_facesWithArea_caled = calFaceAreas(list_vertices,list_faces)
#print(list_facesWithArea_caled)


## phần sắp xếp lại danh sách diện tích
def partition(arr,left,right): # mãng, index bên trái, index bên phải
    pivot=arr[right][0]

    indexPivot=left-1
    for nums in range(left,right):
        if arr[nums][0]<=pivot:
            indexPivot=indexPivot+1
            if indexPivot!=nums: # nếu như vị trị của nó đã đúng thì để yên, nếu vị trí nó sai thì đổi lại
                arr[nums],arr[indexPivot]=arr[indexPivot],arr[nums] # chuyển đổi vị trí nếu nó khác

    arr[indexPivot+1],arr[right]=arr[right],arr[indexPivot+1]

    return indexPivot+1 # trả về index


def quickSort(arr,left,right):

    if left>right:
        return
    index=partition(arr,left,right) #2
    quickSort(arr,left,index-1)# riêng bên trái
    quickSort(arr,index+1,right)# riêng bên phải


def quickSorthaha(arr, left, right):
    print('trái là ', left)
    print('phải là ', right)

    if left > right:
        return
    index = partition(arr, left, right)  # 2
    quickSorthaha(arr, left, index - 1)  # riêng bên trái
    quickSorthaha(arr, index + 1, right)  # riêng bên phải




quickSort(list_facesWithArea_caled,0,len(list_facesWithArea_caled)-1)
##print(list_facesWithArea_caled)
#b=time.time()

min_Face_Area = list_facesWithArea_caled[0]
# và vị trí cuối mảng là -1 sẽ là lớn nhất
max_Face_Area = list_facesWithArea_caled[-1]
# lấy vị trí thứ 0 chính là chỗ lưu diện tích trừ nhau, nếu ra âm càng lớn thì hình hiện tại không mịn, càng nhỏ càng mịn
print(min_Face_Area[0] - max_Face_Area[0])

def makeMidPoints( max_Face, list_vertices_current,list_faces_current):
    # biến này chứa nội dung Face cần chia nhỏ có dạng [v1,v2,v3]
    content_Face =  list_faces_current[ max_Face[1] ]
    # biến này chứa vị trí của Face cần chia đang nằm ở đâu trong danh sách Faces, nó là phần tử thứ 1, nhớ là phần tử thứ 0 chính là diện tích

    index_Face = max_Face[1]

    # đọc xem v1 ở vị trí thứ bao nhiêu gán vào biến index_v1
    index_v1 = content_Face[0]
    # truy cập vào vị trí đó lấy ra tọa độ của v1, nhớ chú ý là khi truy cập vào list Vertices luôn phải trừ 1 như đã nói ở trên
    v1 = list_vertices_current[index_v1 -1]
    # tương tự cho 2 đỉnh còn lại
    index_v2 = content_Face[1]
    v2 = list_vertices_current[index_v2 -1]
    index_v3 = content_Face[2]
    v3 = list_vertices_current[index_v3 -1]

    # tính trung điểm  bằng cách lấy tổng x của 2 đỉnh chia 2, tương tự cho y và z
    mid_v1v2 = [(v1[0] + v2[0])/2,(v1[1] + v2[1])/2,(v1[2] + v2[2])/2 ]
    mid_v2v3 = [(v3[0] + v2[0])/2,(v3[1] + v2[1])/2,(v3[2] + v2[2])/2 ]
    mid_v1v3 = [(v1[0] + v3[0])/2,(v1[1] + v3[1])/2,(v1[2] + v3[2])/2 ]
    # vậy là ta có 3 trung điểm, bây giờ xét xem trung điểm đó có trùng với đỉnh nào trong danh sách đỉnh hiện tại không
    # một biến cờ nhằm báo có nếu như có, ban đầu mặc định là không
    # tạo ra ba biến cờ
    flagv1v2=False
    flagv2v3=False
    flagv1v3 = False
    i=0
    for index_ver in range(len(list_vertices_current)):
        # nếu cả x. y và z giống với một vertice thứ index_ver nào đó thì
        if (mid_v1v2[0] == list_vertices_current[index_ver][0] and
                mid_v1v2[1] == list_vertices_current[index_ver][1] and
                mid_v1v2[2] == list_vertices_current[index_ver][2]):
            flagv1v2=True
            index_mid_v1v2=index_ver+1
            i+=1
        if (mid_v2v3[0] == list_vertices_current[index_ver][0] and
                mid_v2v3[1] == list_vertices_current[index_ver][1] and
                mid_v2v3[2] == list_vertices_current[index_ver][2]):
            flagv2v3 = True
            index_mid_v2v3 = index_ver + 1
            i+=1
        if (mid_v1v3[0] == list_vertices_current[index_ver][0] and
                mid_v1v3[1] == list_vertices_current[index_ver][1] and
                mid_v1v3[2] == list_vertices_current[index_ver][2]):
            flagv1v3 = True
            index_mid_v1v3 = index_ver + 1
            i+=1
        if i==3:
            break
    ### điệu kiện để được đi vào list
    ### có nên tạo hàm bật flag không cho code ngắn đi
    if (flagv1v2 == False):
        list_vertices_current.append(mid_v1v2)
        index_mid_v1v2 = len(list_vertices_current)
    if (flagv2v3 == False):
        list_vertices_current.append(mid_v2v3)
        index_mid_v2v3 = len(list_vertices_current)
    if (flagv1v3 == False):
        list_vertices_current.append(mid_v1v3)
        index_mid_v1v3 = len(list_vertices_current)


        # giờ là thêm 3 faces có chứa vừa trung điểm vừa v vào danh sách faces
    list_faces_current.append([index_mid_v1v2, index_mid_v1v3, index_v1])
    list_faces_current.append([index_mid_v1v2, index_mid_v2v3, index_v2])
    list_faces_current.append([index_mid_v1v3, index_mid_v2v3, index_v3])
    # và face cuối hoàn toàn là do 3 trung điểm tạo thành
    list_faces_current.append([index_mid_v1v2, index_mid_v1v3, index_mid_v2v3])
    # xóa Face lớn đã bị chia nhỏ đi
    list_faces_current.pop(index_Face)
    # trả về danh sách Vertcies đã thêm 3 trung điểm và danh sách Faces đã thêm 4 faces nhỏ
    return list_vertices_current, list_faces_current



copy_listVertices = list_vertices.copy()
copy_listFaces = list_faces.copy()
# truyền 2 danh sách copy đó kèm với Face có diện tích lớn nhất vào xem nó có hoạt động hay không
# tạo 2 biến danh sách Added để mô tả Vertices đã thêm 3 trung điểm và Faces đã thêm 4 faces nhỏ
list_Vertices_Added,list_Faces_Added =  makeMidPoints(max_Face_Area, copy_listVertices, copy_listFaces)


list_facesWithArea_caled = calFaceAreas(list_Vertices_Added,list_Faces_Added)
# sau đó sắp xếp xem các Faces mới sẽ nằm đâu trong thứ tự diện tích
quickSort(list_facesWithArea_caled,0,len(list_facesWithArea_caled)-1)


## Dùng cấu trúc dữ liệu AVL tree


loop_number = 200
for i in range (loop_number):
    # điều chỉnh lại BiG(O)=N
    list_facesWithArea_caled = calFaceAreas(list_Vertices_Added,list_Faces_Added) ### O(n)

    # sắp xếp thêm nlog(n) nữa
    quickSort(list_facesWithArea_caled,0,len(list_facesWithArea_caled)-1) # O(n*log(n))

    b=list_facesWithArea_caled[0][0] - list_facesWithArea_caled[-1][0]
    print(b)

    # và tạo thêm điểm mới nữa
    # O(n)
    # vậy tổng là O(n)*(2+log(n))
    list_Vertices_Added,list_Faces_Added = makeMidPoints(list_facesWithArea_caled[-1], list_Vertices_Added,list_Faces_Added )




# Thuật toán này có một điểm lỗi là không cập nhật lại vị trí thực trên list add face
# bây giờ đã có điểm chứa các điểm và các face mới và có lưu ý rằng những face được tạo ra nó nằm cuối face
# nên ta chỉ cần lấy 4 face mới và tính diện tích sau đó add nó vào face chứa diện tích và cuối cùng là sắp xếp lại
# ta sẽ đẩy mạnh việc sắp xếp bằng cách thêm vào một số khỏi đầu phù hơp trong hàm quick sort






b=time.time()
a=b-c
print('số giây là: ', a)
end_vertice=len(list_Vertices_Added)
print('số điểm là : ',end_vertice-begin)
score=(end_vertice-begin)/a
print('điểm là: ', score)




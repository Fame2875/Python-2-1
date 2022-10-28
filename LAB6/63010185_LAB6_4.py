'''
เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
และให้ระวังเรื่องการสลับ list ให้ดีๆ

หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html

Enter Input : 3
|  |  |
1  |  |
2  |  |
3  |  |
move 1 from  A to C
|  |  |
|  |  |
2  |  |
3  |  1
move 2 from  A to B
|  |  |
|  |  |
|  |  |
3  2  1
move 1 from  C to B
|  |  |
|  |  |
|  1  |
3  2  |
move 3 from  A to C
|  |  |
|  |  |
|  1  |
|  2  3
move 1 from  B to A
|  |  |
|  |  |
|  |  |
1  2  3
move 2 from  B to C
|  |  |
|  |  |
|  |  2
1  |  3
move 1 from  A to C
|  |  |
|  |  1
|  |  2
|  |  3

'''

sA = ['A']
sB = ['B']
sC = ['C']
u = 0


def move(n, A, B, C):
    if (n > 0):
        move(n - 1, A, C, B)
        print("move %d from  %s to %s" % (n, A[0], C[0]))
        ind = A.index(n)
        C.insert(1, A[ind])
        C.pop()
        A[ind] = 0
        charA = A.pop(0)
        charC = C.pop(0)
        A.sort(reverse=True)
        C.sort(reverse=True)
        A.insert(0,charA)
        C.insert(0,charC)
        show_list(u, sA, sB, sC)
        move(n - 1, B, A, C)


def fill_stack(n, A, B, C):
    if n != 0:
        A.append(int(n))
        B.append(int(0))
        C.append(int(0))
        fill_stack(n - 1, A, B, C)
    else:
        A.append(int(0))
        B.append(int(0))
        C.append(int(0))


def show_list(n, A, B, C):
    if n != 0:
        print("{}  {}  {}".format(A[n + 1] if A[n + 1] != 0 else '|', B[n + 1] if B[n + 1] != 0 else '|', C[n + 1] if C[n + 1] != 0 else '|'))
        show_list(n - 1, A, B, C)
    else:
        print("{}  {}  {}".format(A[n + 1] if A[n + 1] != 0 else '|', B[n + 1] if B[n + 1] != 0 else '|', C[n + 1] if C[n + 1] != 0 else '|'))


n = int(input("Enter Input : "))
u = n
fill_stack(n, sA, sB, sC)
show_list(u,sA,sB,sC)
move(n, sA, sB, sC)
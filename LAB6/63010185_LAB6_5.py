'''
นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

Enter Input : -2, -1, 1, 2
[-2, -1, 1, 2]
Enter Input : -2, 1, 1, -2
[-2, -2]
'''
def asteroid_collision(asts):
    if len(asts) == 1:
        return asts

    results = asteroid_collision(asts[1:])

    if len(results) > 0 and asts[0] > 0 and results[0] < 0:
        # not normal case (len(results) > 0 for the first case that results size can be 0)

        if asts[0] == abs(results[0]):  # same size .. 2 exploded
            if len(results) > 1:
                return results[1:]  # get the rest back from right
            elif len(results) == 1:
                return []  # nothing left

        elif asts[0] > abs(results[0]):  # left has more than right... right exploded
            return asteroid_collision([asts[0]] + results[1:])

        elif asts[0] < abs(results[0]):  # left has less than right... left exploded
            return results  # right and get the rest back

    else:
        # normal case
        return [asts[0]] + results  # return data back...


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))
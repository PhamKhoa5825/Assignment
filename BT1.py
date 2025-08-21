def solve(thoiTiet, sucKhoe, tamTrang, thoiGian,
          doQuanTrong1, doQuanTrong2, doQuanTrong3, doQuanTrong4):
    if thoiTiet == "1" and sucKhoe == "1" and tamTrang == "1" and thoiGian == "0":
        decide = "Đi học"
    elif doQuanTrong1 == "1" or doQuanTrong2 == "1" or doQuanTrong3 == "1" or doQuanTrong4 == "1":
        decide = "Đi học"
    else:
        decide = "Nghỉ"
    return decide

def main():
    print("Hello")
    print("Hệ chuyên gia sẽ giúp bạn đưa ra quyết định: ")
    print("HÔM NAY CÓ NÊN ĐI HỌC HAY KHÔNG?")
    print("Bạn hãy trả lời các câu sau: Có -> 1, Không -> 0")

    thoiTiet = input("Thời tiết hôm nay có đẹp không?(1/0) ")
    sucKhoe = input("Bạn có khoẻ không?(1/0) ")
    tamTrang = input("Tâm trạng của bạn có tốt không?(1/0) ")
    thoiGian = input("Bạn đã trễ giờ chưa?(1/0) ")
    doQuanTrong1 = input("Môn này có quan trọng không?(1/0) ")
    doQuanTrong2 = input("Bài hôm nay có quan trọng không?(1/0) ")
    doQuanTrong3 = input("Hôm nay có kiểm tra không?(1/0) ")
    doQuanTrong4 = input("Bạn có ngại học lại môn này không?(1/0) ")

    print("Chuyên gia tư vấn là:")
    decide = solve(thoiTiet, sucKhoe, tamTrang, thoiGian,
                   doQuanTrong1, doQuanTrong2, doQuanTrong3, doQuanTrong4)
    print("   Bạn nên ", decide)

if __name__ == "__main__":
    main()

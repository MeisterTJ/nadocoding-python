# 사용자 시나리오
# 1. 사용자는 합치려는 이미지를 1개 이상 선택한다.
# 2. 합쳐진 이미지가 저장될 경로를 지정한다.
# 3. 가로넓이, 간격, 포맷 옵션을 지정한다.
# 4. 시작 버튼을 통해 이미지를 합친다.
# 5. 닫기 버튼을 통해 프로그램을 종료한다.

# 기능 명세
# 1. 파일추가 : 리스트 박스에 파일 추가
# 2. 선택삭제 : 리스트 박스에서 선택된 항목 삭제
# 3. 찾아보기 : 저장 폴더를 선택하면 텍스트 위젯에 입력
# 4. 가로넓이 : 이미지 넓이 지정 (원본유지, 1024, 800, 640)
# 5. 간격 : 이미지 간의 간격 지정 (없음, 좁게, 보통, 넓게)
# 6. 포맷 : 저장 이미지 포맷 지정 (PNG, JPG, BMP)
# 7. 시작 : 이미지 합치기 작업 실행
# 8. 진행상황 : 현재 진행중인 파일 순서에 맞게 반영
# 9. 닫기 : 프로그램 종료
import os  # 경로 사용
import tkinter.ttk as ttk  # 콤보 박스, 프로그레스 바
import tkinter.messagebox as msgbox  # 메시지 박스
from tkinter import *  # __all__
from tkinter import filedialog  # __all__에 파일 다이얼로그가 포함되어있지 않다.
from PIL import Image

root = Tk()
root.title("Nado GUI")
root.resizable(False, False)  # x, y 창 크기 변경 불가


# 파일 추가 함수
def add_file():
    # 복수 개의 파일을 선택한다.
    # filetypes : 파일 확장자
    # initialdir : 최초로 보여줄 디렉토리 (r을 쓰면 escape 문자 상관없이 그대로 쓴다는 의미 raw string)
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요"
                                        , filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*"))
                                        ,
                                        initialdir=r"C:\Users\chogdak\PycharmProjects\nadocoding\gui_project")
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)


# 선택 삭제
def del_file():
    # print(list_file.curselection())
    # 지울 때는 뒤의 인덱스부터 지워야한다. 이유는 앞에서 지우면 인덱스 문제로 엄한게 지워질 수 있다.
    for index in reversed(list_file.curselection()):  # curselection()은 선택한 파일들의 인덱스를 시퀀스로 반환한다.
        list_file.delete(index)


# 저장 경로 (폴더 선택)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is "":
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


# 이미지 통합
def merge_image():
    try:
        # 가로 넓이
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1  # -1 일때는 원본 기준으로
        else:
            img_width = int(img_width)  # 정수형으로 변환

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif  img_space == "넓게":
            img_space = 90
        else:   # 없음
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower()   # 소문자로 변환

        # print(list_file.get(0, END))    # 모든 파일 목록을 가지고 오기
        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = [] # (width1, height1), (width2, height2), ...
        if img_width > -1:  # 정해진 width로 비율을 맞춰야 한다
            # 100 * 60 -> width가 80일경우 -> 80 * 48( x`y / x )
            # width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:   # 원본 유지
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # 해당 이미지의 size -> size[0] : width, size[1] : height
        # 모든 이미지의 전체 높이를 알고, 가장 width가 큰 이미지를 기준으로 한다.
        # widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]

        # [(10, 10), (20, 20), (30, 30)] <- x.size의 값 구성
        widths, heights = zip(*image_sizes)  # unzip으로 가져오기

        # 가장 큰 너비, 토탈 높이
        max_width, total_height = max(widths), sum(heights)

        # 스케치북 준비
        if img_space > 0:   # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) - 1))

        result_image = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0  # y 위치

        # for image in images:
        #     result_image.paste(image, (0, y_offset))
        #     y_offset += image.size[1]   # height 값 만큼 더해준다.
        # 실제 이미지를 합치는 작업
        for idx, image in enumerate(images):
            # width 가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                image = image.resize(image_sizes[idx])

            result_image.paste(image, (0, y_offset))
            y_offset += (image.size[1] + img_space)     # height + 간격 옵션

            progress = (idx + 1) / len(images) * 100  # 실제 진행 퍼센트 계산
            p_var.set(progress)
            progress_bar.update()  # 프로그레스 바 설정

        # 포맷 옵션 처리
        file_name = "nado_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_image.save(dest_path)  # 이미지를 저장한다.
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err:    # 예외 처리 (퍼미션, 없는 디렉토리 등)
        msgbox.showerror("에러", err)


# 시작 버튼
def start():
    # 파일 목록 확인
    if list_file.size() is 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) is 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요.")
        return

    # 이미지 통합 작업
    merge_image()


# [파일 프레임] (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="파일추가", padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5, width=12, command=del_file)
btn_del_file.pack(side="right")

# [리스트 프레임]
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

# 파일 15개까지 볼 수 있고, 복수 선택 가능
list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# [저장 경로 프레임]
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
# ipad : 안쪽 패딩, entry 영역이 조금 높아진다.
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# [옵션 프레임]
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5)

# 1. 이미지 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# [진행 상황 프레임] Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# [실행 프레임]
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()
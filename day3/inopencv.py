import cv2

# 비디오 파일 열기
video_path = 'test_video.mp4'
cap = cv2.VideoCapture(video_path)

# 비디오 파일이 제대로 열렸는지 확인
if not cap.isOpened():
    print("비디오 파일을 열 수 없습니다. 경로를 확인하세요.")
else:
    # 프레임을 순차적으로 읽어서 출력
    while True:
        ret, frame = cap.read()  # 한 프레임 읽기
        if not ret:
            print("비디오가 끝났거나 오류가 발생했습니다.")
            break

        # 프레임 출력
        cv2.imshow('Video Frame', frame)

        # 키 입력 대기 (1ms 대기 후 다음 프레임)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
            break

    # 비디오 객체 해제
    cap.release()

# 모든 창 닫기
cv2.destroyAllWindows()
from win10toast import ToastNotifier

def show_notification(message):
    toaster = ToastNotifier()
    toaster.show_toast("알림", message, duration=10)

def main():
    message = input("알림 메시지를 입력하세요: ")
    show_notification(message)

if __name__ == "__main__":
    main()

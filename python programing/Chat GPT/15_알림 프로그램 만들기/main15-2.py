from win10toast import ToastNotifier
import schedule
import time

def show_notification():
    toaster = ToastNotifier()
    toaster.show_toast("알림", "회의 시작 10분전입니다.", duration=10)

def schedule_notification():
    schedule.every().monday.at("09:50").do(show_notification)
    schedule.every().wednesday.at("09:50").do(show_notification)
    schedule.every().friday.at("09:50").do(show_notification)

def main():
    schedule_notification()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

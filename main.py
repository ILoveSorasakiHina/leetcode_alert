import time,easygui,logging
from apscheduler.schedulers.background import BackgroundScheduler

#設定該module的logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#用檔案紀錄logger輸出
handler = logging.FileHandler("scheduler.log")

#設定logger輸出格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

def daily_challenge():
    #彈出提醒視窗
    try:
        easygui.msgbox("The daily challenge has been refreshed! Please solve the challenge.")
        logger.info('Daily challenge reminder sent.')
    except Exception as e:
        logger.error('Error daily challenge: %s', e)


def week_contest():
    try:
        easygui.msgbox("The leetcode contest will start at 10:30 A.M. Please prepare.")
        logger.info('Weekly contest reminder sent.')
    except Exception as e:
        logger.error('Error week contest: %s', e)



#創建物件，記得設定時區
scheduler = BackgroundScheduler(timezone="Asia/Taipei")

#省略tragger可以立刻運行
#從某日8點開始計算，間隔一天運行，每天8點會自動執行函數
scheduler.add_job(daily_challenge,"interval", days=1, start_date="2024-07-27 11:59:00")
#每周日10點20分自動執行函數
scheduler.add_job(week_contest, "cron", day_of_week = "6", hour = 10, minute = 20)

try:
    scheduler.start()
except Exception as e:
    print(e)
    logger.error('Error starting scheduler: %s', e)


# 讓程式持續執行，透過sleep節省cpu
while True:
    time.sleep(1)
    

    

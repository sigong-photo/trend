#!/usr/bin/env python3
"""
놀 티켓(NOL TICKET) 오픈예정 공연 매일 오전 6시 자동 수집 스케줄러
URL: https://nol.yanolja.com/ticket/display/upcoming?genre=concert
"""

import os
import sys
import time
from datetime import datetime, timedelta
from collector import save_topics

def run_collection():
    print(f"\n========================================================")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ⏰ 놀 티켓 오픈예정 공연 정기 수집 시작")
    print(f"========================================================")
    try:
        new_count = save_topics()
        if new_count > 0:
            print(f"🎉 신규 공연 {new_count}건이 새로 등록되었습니다!")
        else:
            print(f"ℹ️ 새로운 공연이 없습니다. (기존 목록 최신 상태 유지)")
    except Exception as e:
        print(f"❌ 수집 중 오류 발생: {e}")

def get_seconds_until_next_run(target_hour=6, target_minute=0):
    now = datetime.now()
    target = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return (target - now).total_seconds(), target

def main():
    print("🚀 놀 티켓 매일 오전 06:00 자동 수집 데몬이 시작되었습니다.")
    print("   매일 오전 6시에 https://nol.yanolja.com/ticket/display/upcoming?genre=concert 를 확인하여 새 공연을 등록합니다.\n")

    # 시작 시 즉시 1회 확인
    run_collection()

    while True:
        wait_seconds, next_run = get_seconds_until_next_run(6, 0)
        print(f"\n💤 다음 자동 수집 예정 시각: {next_run.strftime('%Y-%m-%d %H:%M:%S')} (약 {wait_seconds / 3600:.1f}시간 후 대기)")
        
        # 1시간 단위로 체크하면서 대기
        while wait_seconds > 0:
            sleep_step = min(wait_seconds, 3600)
            time.sleep(sleep_step)
            wait_seconds -= sleep_step

        run_collection()

if __name__ == "__main__":
    main()

# 로그 남기기
import logging
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
#
# logging.debug("아 이거 누가 짠거야~~")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 오래 되었습니다.")
# logging.error("에러 발생")
# logging.critical("치명적인 문제")

# 터미널과 파일에 함께 로그 남기기
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)    # 로거에 스트림핸들러를 추가

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")    # mylog_20201010141011.log
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)      # 로거에 파일 핸들러를 추가

logger.debug("로그를 남겨보는 테스트2")   # 로거는 스트림, 파일 핸들러로 출력
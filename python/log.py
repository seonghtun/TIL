import logging

#logging.basicConfig(filename="example.log", level=logging.WARNING)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')
#logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

#logging.basicConfig(
#    format='%(asctime)s %(levelname)s:%(message)s',
#    level=logging.DEBUG,
#    datefmt='%m/%d/%Y %I:%M:%S %p',
#)
#
#logging.debug("Sample debug message")


#logger = logging.getLogger("postprocessor")
#logger.setLevel(logging.DEBUG)
#
#logger = logging.getLogger("postprocessor.skeleton")
#logger.setLevel(logging.NOTSET)
#
#print(logger.getEffectiveLevel() == logging.DEBUG)

#logger = logging.getLogger("postprocessor.skeleton")
#logger.setLevel(logging.WARNING)
#logger.info("Skeleton module logger test!")

# 로거 세팅
#logger = logging.getLogger("postprocessor")
#logger.setLevel(logging.DEBUG)
#
## 일반 핸들러, 포매터 세팅
#formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
#handler = logging.StreamHandler()
#handler.setFormatter(formatter)
#
## 크리티컬 이벤트에 대한 핸들러, 포매터 세팅
#formatter_critical = logging.Formatter("!!!!!%(asctime)s %(levelname)s:%(message)s")
#handler_critical = logging.FileHandler("log_event.log")
#handler_critical.setLevel(logging.CRITICAL)
#handler_critical.setFormatter(formatter_critical)
#
## 각 핸들러를 로거에 추가
#logger.addHandler(handler)
#logger.addHandler(handler_critical)
#
#logger.info("Is working well?")
#logger.critical("It's not working well.")

# 로거 설정
logger_preprocess = logging.getLogger("preprocess")
logger_postprocess = logging.getLogger("postprocess")

# 포매터, 필터 설정
formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
filter = logging.Filter("preprocess")

# 핸들러 설정
handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.addFilter(filter)

# 핸들러 추가
logger_preprocess.addHandler(handler)
logger_postprocess.addHandler(handler)

logger_preprocess.critical("Critical from preprocess.")
logger_postprocess.critical("Critical from postprocess.")


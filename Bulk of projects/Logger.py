import logging

def LogInfo(message):
	try:
		logging.basicConfig(filename='/var/log/rtrtr-lb.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
		logger = logging.getLogger()
		logger.info(message)

	except Exception as e:
		print (e)

def LogDebug(message):
	try:
		logging.basicConfig(filename='/var/log/rtrtr-lb.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
		logger = logging.getLogger()
		logger.debug(message)

	except Exception as e:
		print (e)

def LogWarning(message):
	try:
		logging.basicConfig(filename='/var/log/rtrtr-lb.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
		logger = logging.getLogger()
		logger.warning(message)

	except Exception as e:
		print (e)

def LogError(message):
	try:
		logging.basicConfig(filename='/var/log/rtrtr-lb.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
		logger = logging.getLogger()
		logger.error(message)

	except Exception as e:
		print (e)

def LogCritical(message):
	try:
		logging.basicConfig(filename='/var/log/rtrtr-lb.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
		logger = logging.getLogger()
		logger.critical(message)

	except Exception as e:
		print (e)



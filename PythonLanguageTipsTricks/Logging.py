# Basic Logging Basic Logging Basic Logging Basic Logging Basic Logging Basic Logging Basic Logging  
import logging
logging.info('infoinfoinfoinfoinfoinfo')
logging.debug('debug')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

# Setting minimum logging level required
logging.basicConfig(level=logging.DEBUG) # this method should be invoked only once per app !

# Setting destination of logs
logging.basicConfig(filename='jakistamplik.log') # this method should be invoked only once per app !



# Customized Logging Customized Logging Customized Logging Customized Logging Customized Logging 
# check out doc of the basicConfig methods, it has many interesting things to set up
# for example : date, format, filemode, trace, method name that invoked logging, 
# this method (basicConfig) should be invoked only once per app !
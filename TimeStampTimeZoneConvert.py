# Converts a timestamp from a source timezone to destination timezone. i.e. UTC to EST5EDT

from dateutil import tz

class TimeStampConvertTimeZone(object):
	  def __init__(self):
		  pass
    
    def convertTimetz(self, from_zone, to_zone, fmt, utcTimeStr=''):
      print 'From: ' + utcTimeStr
      utc = datetime.strptime(utcTimeStr, fmt)
      utc = utc.replace(tzinfo=from_zone)
      easternDt = utc.astimezone(to_zone)
      easternStr = easternDt.strftime(fmt)
      print 'To: ' + easternStr
      return easternStr

if __name__ = "__main__":
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')
    fmt = '%Y-%m-%d %H:%M:%S.%f'
    utcTimeStr = '2016-07-04 16:43:23.69300'
    timeData = TimeStampConvertTimeZone()
    timeData.convertTimetz(from_zone, to_zone, fmt, utcTimeStr)

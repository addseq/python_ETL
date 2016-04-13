# Sample Input:	{"_id":{"$oid":"12345"},"pageName":"Google","pageURL":"http://www.google.com","userId":"user123","lenthOfStay":5,"accessTime":{"$numberLong":"1460586107266"}}
# Sample Output:	Google|"http://www.google.com"|user123|5|-4|2016/04/13 18:21:47.266
import time
import json

class JsonDeserializer(object):
	def __init__(self):
		pass
	
	def decodeJsonAndTimestamp(self):
	# Decodes json and unix timestamp to a list
	f = open("C:/MyFiles/webData.json",'rb')
	utc_offset = time.localtime().tm_hour - time.gmtime().tm_hour
	webDataList = []
	for row in f:
		p = JsonToDict(row)
		timeStr = str(p.accessTime['$numberLong'])
		timeUnix = timeStr[:-3]
		timeMillis = timeStr[-3:]
		formattedTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(int(timeUnix))) + '.' + timeMillis
		webData = p.pageName + '|' p.pageURL + '|' + p.userId + '|' + str(int(round(p.lenthOfStay,0))) + '|' + str(utc_offset) + '|' + formattedTime
		webDataList.append(webData.strip())
	f.close()
	
	# Determine how many output files are needed, each of size maxRowsOutFile
	maxRowsOutFile = 3
	startIdx = 1
	endIdx = maxRowsOutFile
	webDataSize = len(webDataList)
	modOutFile = webDataSize % maxRowsOutFile
	numOutFiles = webDataSize // maxRowsOutFile
	if (modOutFile > 0):
		numOutFiles += 1
	print 'Min Output files required: ' + str(numOutFiles)
	
	# For each output file, slice the list for max # of rows and write to file
	for partfile in range(startIdx, numOutFiles+1):
		outFile = "C:/MyFiles/decoded_webJson_" + str(partFile) + ".dat"
		f = open(outFile, 'wb')
		print 'Writing rows ' + str(startIdx) + '-' + str(endIdx) + ' to file: [' + outFile + ']'
		webDataSlice = webDataList[startIdx-1 : endIdx]
		#print 'Size of Outfile Part: ' + str(len(webDataSlice))
		for row in webDataSlice:
			f.write(row+'\n')
		f.close()
		startIdx += maxRowsOutFile
		endIdx += maxRowsOutFile
		if(endIdx > webDataSize):
			endIdx = endIdx - maxRowsOutFile + modOutFile
		print 'Sucessfully written all rows to file!'
		
class JsonToDict:
	def __init__(self, x):
		self.__dict__ = json.loads(x)
	
if __name__ = "__main__":
	jsonData = JsonDeserializer()
	jsonData.decodeJsonAndTimestamp()
	

	
	
import urllib
import urllib2
import cookielib
import re


class Uestc:
	def __init__(self):
		self.loginUrl = 'https://uis.uestc.edu.cn/amserver/UI/Login?goto=http%3A%2F%2Fportal.uestc.edu.cn%2Flogin.portal'
		# semester 2014-2015-1
		self.gradeUrl = '' #'http://eams.uestc.edu.cn/eams/teach/grade/course/person!search.action?semesterId=43&projectType='
		self.cookies = cookielib.CookieJar()
		self.postdata = urllib.urlencode({
				'IDToken1': 'stuid',
				'IDToken2': 'pwd'
			})
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
		self.grade =[]
		self.credit = []


	def getPage(self):
		req = urllib2.Request(
			url = self.loginUrl,
			data = self.postdata)
		reslut = self.opener.open(req)
		reslut = self.opener.open(self.gradeUrl)

		return reslut.read()

	def getGrades(self):
		page = self.getPage()
		myItems = re.findall('<tr.*?<td.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?<td.*?<td.*?>(.*?)</td>.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>', 
			page, re.S)
		for item in myItems:
			print 'The score of {0} is {1}. ({2}/{3})'.format(item[0].strip(), item[2].strip(), item[3].strip(), item[1].strip())

uestc = Uestc()
uestc.getGrades()


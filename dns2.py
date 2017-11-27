import subprocess

resolvers = {'google': '8.8.8.8', 'opendns': '208.67.222.222', 'dyn': '216.146.35.35', 'qaud9': '9.9.9.9', 'level3': '209.244.0.3', 'verisign': '64.6.64.6'}
urls = ['www.youtube.com',
'www.facebook.com',
'www.baidu.com',
'www.yahoo.com',
'www.amazon.com',
'www.wikipedia.org',
'www.qq.com',
'www.google.co.in',
'www.twitter.com',
'www.live.com',
'www.taobao.com',
'www.bing.com',
'www.instagram.com',
'www.weibo.com',
'www.sina.com.cn',
'www.linkedin.com',
'www.yahoo.co.jp',
'www.msn.com',
'www.vk.com',
'www.google.de',
'www.yandex.ru',
'www.hao123.com',
'www.google.co.uk',
'www.reddit.com',
'www.ebay.com',
'www.google.fr',
'www.t.co',
'www.tmall.com',
'www.google.com.br',
'www.360.cn',
'www.sohu.com',
'www.amazon.co.jp',
'www.pinterest.com',
'www.netflix.com',
'www.google.it',
'www.google.ru',
'www.microsoft.com',
'www.google.es',
'www.wordpress.com',
'www.gmw.cn',
'www.tumblr.com',
'www.paypal.com',
'www.blogspot.com',
'www.imgur.com',
'www.stackoverflow.com',
'www.aliexpress.com',
'www.naver.com',
'www.ok.ru',
'www.apple.com',
'www.github.com',
'www.chinadaily.com.cn',
'www.imdb.com',
'www.google.co.kr',
'www.fc2.com',
'www.jd.com',
'www.blogger.com',
'www.163.com',
'www.google.ca',
'www.whatsapp.com',
'www.amazon.in',
'www.office.com',
'www.tianya.cn',
'www.google.co.id',
'www.youku.com',
'www.rakuten.co.jp',
'www.craigslist.org',
'www.amazon.de',
'www.nicovideo.jp',
'www.google.pl',
'www.soso.com',
'www.bilibili.com',
'www.dropbox.com',
'www.xinhuanet.com',
'www.outbrain.com',
'www.pixnet.net',
'www.alibaba.com',
'www.alipay.com',
'www.microsoftonline.com',
'www.booking.com',
'www.googleusercontent.com',
'www.google.com.au',
'www.popads.net',
'www.cntv.cn',
'www.zhihu.com',
'www.amazon.co.uk',
'www.diply.com',
'www.coccoc.com',
'www.cnn.com',
'www.bbc.co.uk',
'www.twitch.tv',
'www.wikia.com',
'www.google.co.th',
'www.go.com',
'www.google.com.ph',
'www.doubleclick.net',
'www.onet.pl',
'www.googleadservices.com',
'www.accuweather.com',
'www.googleweblight.com',
'www.answers.yahoo.com']

class DnsBench:
	def __init__(self, resolver, resolver_name, urls):
		self.resolver = resolver
		self.resolver_name = resolver_name
		self.urls = urls
		self.response_times = []

	def perform_query(self):
		print("resolving {} ..".format(self.resolver_name))
		for url in urls:
			try:
				response_time = int(subprocess.check_output('dig @{}  {} | grep "Query time" | grep -Eo "[0-9]+"'.format(self.resolver,url), shell=True))
				self.response_times.append(response_time)

			except:
				pass
		print(self.mean(self.response_times))

	def mean(self, response_times):
		total = sum(response_times)
		num = len(response_times)
		return float(total/num)



for name, addr in resolvers.items():
	dnsb = DnsBench(addr, name, urls)
	dnsb.perform_query()


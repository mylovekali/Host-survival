for i in range(1,255):
	try:
		url = "http://192-168-1-" + str(i) + ".awd.bugku.cn/e/search/result/1.php"
		print(url)
	except:
		pass		

//单线程扫描C段存活
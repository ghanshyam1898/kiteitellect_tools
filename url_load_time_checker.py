import requests
import urllib


def check_kiteintellect_sse(url):
	if not url.startswith("http"):
		url = "http://" + url

	request = urllib.request.Request(url)
	request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')
	response = urllib.request.urlopen(request)

	server =  response.getheader('Server')

	if server.lower() != "kiteintellect":
		print("\n\nThe website is not using Kite Intellect SSE currently. Server header returned is : {}\n\n".format(server))

	else:
		print("\n\nThe website uses Kite Intellect SSE\n\n")


def measure_load_time(url, number_of_hits=5, also_check_kiteintellect_sse = False):
	if also_check_kiteintellect_sse is True:
		check_kiteintellect_sse(url)

	if not url.startswith("http"):
		url = "http://" + url

	total_time = 0
	time_per_hit = []

	for i in range(1, number_of_hits + 1):
		try:
			data = requests.get(url, allow_redirects=False)
			time = data.elapsed.total_seconds()			
			time_per_hit.append(time)
			total_time += time

			print("Hit {} took {} time and returned response code : {}".format(i, time, data.status_code))

		except Exception as e:
			print("Following error occurred : {}".format(e))

	print("\nFollowing are the response timings : {}".format(time_per_hit))
	print("\n\n*** Average load time of given url is : {} ***".format(total_time/ number_of_hits))


if __name__ == '__main__':
	url = input("Enter the url : ")
	also_check_kiteintellect_sse = input("Press any key and then press enter to not check kiteintellect sse status : ")
	if len(also_check_kiteintellect_sse) > 0:
		also_check_kiteintellect_sse = False
	else:
		also_check_kiteintellect_sse = True

	if not url.startswith("http"):
		url = "http://" + url

	measure_load_time(url, also_check_kiteintellect_sse=also_check_kiteintellect_sse)
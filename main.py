import requests
from bs4 import BeautifulSoup
URL = "https://pythonjobs.github.io/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#print(soup) //works this prints the whole html code for the webpage
allJobs = soup.find("section",class_="job_list")#//I have got all the jobs listed in this page on this line


job_elements = allJobs.find_all("div", class_="job")
#print(job_elements,end="\n"*2) #//prints on the jobs
for job_element in job_elements:
    job_title = job_element.find("h1")
    print("Job-Title: "+job_title.text)


    allSpans = job_element.find_all("span")
    print("Company Location: "+allSpans[0].text)
    print("Job posted on : " + allSpans[1].text)
    print("Job Type: " + allSpans[2].text)
    print("Company Name: " + allSpans[3].text)


    link = job_element.find("a")["href"]
    print("Job link: "+link, end="\n"*3)
    """
    print("Company Location: "+allSpans[0].text)
    print("Job posted on: " + allSpans[1].text)
    print("Job Type: " + allSpans[2].text)
    print("Company Name: " + allSpans[3].text)
    """
    #company_location = job_element.find("span", class_="info")
    #print("Company location: "+company_location)






''' since selenium is so fast it is difficult to see
 it work in real-time so we use time to delay the program
  and wait for us to see what is it doing and ofcouse to
   witness the beauty of automation.that is why we use this 
   time module in python. 
'''
from os import pipe
import time
from socket import timeout # it is used to connect a client and a server
from selenium import webdriver # the holy webdriver to control all all the commands
from selenium.webdriver.common import alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("\n\nHello, welcome to the automated security scanner:\n\n")

print("Select security level for the testing website.\n")
print("1.Low \n2.Medium \n3.High \n4.IMPOSSIBLE\n\n")
print("note: \n 1.Low: This security level is completely vulnerable and has no security measures at all.")
print("\n 2.Medium: This setting is mainly to give an example to the user of bad security practices, where the developer has tried but failed to secure an application.")
print("\n 3.High:This option is an extension to the medium difficulty, with a mixture of harder or alternative bad practices to attempt to secure the code.")
print("\n 4.IMPOSSIBLE: This level should be secure against all vulnerabilities.\n\n")

print("Select the desired threat level: ")
threat_level = 0
while 1 > threat_level or 4 < threat_level:
    try:
        # to give user one more chance to select the input
        threat_level = int(input("\nPlease enter your threat_level within range (1 - 4) : "))

        #for selecting the therat level for the website.
        switcher = {
            1:'low',
            2: 'medium',
            3: 'high',
            4: 'impossible'
        }

        threat = switcher.get(threat_level, "\nsecurity NOT set.")
    except ValueError:
        # Remember, not everyone is a developer.
        print ("That wasn't an integer.")

print("Selected security level is ",threat)

#to see the execution in real time 
#if yes the execution will be delayed by 2 secs 
delay = 0
time_select = ""
print("\nDo you want to see the execution? y/n")

#for selecting only one of the above options
# if time_select in ("y","n","Y","N"):#== "y" or time_select == "Y" or time_select == "n" or time_select == "N":
try:
    #switcher will be used to clean the code in the next step
    time_select = input("\nplease enter your choice (y/n): ")

    switcher = {
        "y":2,
        "n":0,
        "Y":2,
        "N":0
    }

    delay = switcher.get(time_select, "SELECTION INVALID")
except ValueError:
    #just in case 
    print("That wasn't a 'y' or 'n'. " )    
'''else:
    print("can't find input.")'''
if (delay == 0):
    print ("light speed aheaddd...")

else:
    print("human speed selected.")
# this must be targeted to the webdriver installation folder
PATH = "D:\Installed_Programs\chromedriver.exe"
driver = webdriver.Chrome(PATH) #storing the webdriver in a variable

# this is the target website 
driver.get("http://127.0.0.1/dvwa/") #this time its an custom made website to test web threats.
print("\n\n")

#login into the vulnerable website using the configured pass and username  using link with driver to get the element
link = driver.find_element_by_name("username")
link.click()
link.send_keys("admin")
time.sleep(delay)

#the credentials are set on the device config file prior to website execution see documentation for setup
link = driver.find_element_by_name("password")
link.click()
link.send_keys("password")
time.sleep(delay)

#this was an easy click
submit = driver.find_element_by_name("Login")
time.sleep(delay)

submit.click()


# here we initiated a wait to wait for the page to load before executing judgement we also could have not used it.
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "DVWA Security"))
)
time.sleep(delay)
element.click()

# to select the security level of the website.
select = Select(driver.find_element_by_name('security'))
time.sleep(delay)

#this is the place to select the threat level of the users 
select.select_by_value(threat)
driver.find_element_by_name("seclev_submit").click()

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "XSS (Reflected)"))
)
element.click()
time.sleep(delay)



link = driver.find_element_by_name("name")
link.click()
link.send_keys('<script>alert("This can be hacked!")</script>')
time.sleep(delay)



driver.find_element_by_xpath('//*[@id="main_body"]/div/div/form/p/input[2]').click()
try:
    alert = driver.switch_to.alert
    time.sleep(delay)
    print(alert.text) 
    alert.accept()

except:
    print ("This page is safe from XSS.")


time.sleep(delay)
driver.quit()

from libxenon import *

#functions from libxenon===>
    #login(url,email,password)
    #join_meet(url)
    #print_status(Bool,sring)
    #parse_config()

def main():
    url = "https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3AgidhHrv8tf9Y-NItUcNUlipQpIwYaied8nfhGzdFpYY1%40thread.tacv2%2F1642324424304%3Fcontext%3D%257b%2522Tid%2522%253a%2522161a86cc-cc0c-4622-b590-d0b92db751fe%2522%252c%2522Oid%2522%253a%2522d36a1c19-ce64-4501-9f63-6218f74c433e%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=6cc606b1-e851-4809-ab32-0f93784f9bb2&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true"


#start webdriver
    print_status(True,"Starting webdriver....")


    ehh = parse_config()
    if ehh == None:
        exit
    else:
        a,b = login(ehh['url'], ehh['email'] ,ehh['password'])
        print_status(a,b)
        if a:
            join_meet(url);

if __name__ == "__main__":
    main()

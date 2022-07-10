# Required Packages
import requests
import random
import shutil
import time
import os


# Terminal Cleaner
def Clear_Terminal():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


# Some outside of the built-in library auto-installer (For user convenience)
try:
    import yaml
except ModuleNotFoundError:
    try:
        print("Missing Required Package. Automatically Installing It For You.\n")
        os.system("python -m pip install pyyaml")
    except:
        print(f'\n\nError Occurred... Please Manually Install yaml Module By Typing:\n"pip install pyyaml"')
        exit()

def Main():
    Clear_Terminal()

    # Opens the hidden file created by this script for templates
    with open(".Settings.yaml", "r") as Reader:
        Process = yaml.safe_load(Reader)
        Default_Loop_Value = Process["Settings"]["Script_Override"]["Default_Loop_Value"]
        Site_Protocol = Process["Settings"]["Script_Override"]["Site_Protocol"]
        Script_Password = Process["Settings"]["Script_Override"]["Script_Password"]
        Default_Path = Process["Settings"]["Script_Override"]["Default_Path"]
        Static_Yiff_Link = Process["Settings"]["Website_Data"]["Static_Yiff_Link"]
        Timeout = Process["Settings"]["Website_Data"]["Timeout"]
        Ping = Process["Settings"]["Website_Ping_Data"]["Ping"]
        Proxies = Process["Settings"]["Fake_Credentials"]["Proxies"]
        User_Agent = Process["Settings"]["Fake_Credentials"]["User_Agents"]

    if Script_Password == "":
        pass
    else:
        def Wall():
            Clear_Terminal()
            Prompt = input("Enter Your Script Password:\n >>> ")
            if Prompt == Script_Password:
                Clear_Terminal()
                Downloader()
            else:
                print("\nSorry Wrong Password. Please Try Again.")
                time.sleep(3)
                Wall()
        Wall()

    # Checks User Connection To Avoid More Errors And Issues
    def Check_User_Internet_Connection_Status():
        print("Checking For Your Internet Connection Status...")
        try:
            if requests.get(url=Ping, data=random.choice(User_Agent), proxies={f'{Site_Protocol}': f'{Site_Protocol}://{random.choice(Proxies)}'}, timeout=Timeout) == 200:
                pass
        except (requests.RequestException, requests.ConnectTimeout, requests.ConnectionError):
            print("You Ate Probably Offline, Please Check Your Internet Connection First The Re-Run This script")
            exit()

    # Downloader
    def Downloader():
        Check_User_Internet_Connection_Status()
        Clear_Terminal()
        Comic_Link = input("Enter Your Yiffer.XYZ Porn Link:\n >>> ")
        print("\nProcessing...\n")
        Comic_Download_Link = f'{Static_Yiff_Link}{Comic_Link.split("/")[-1]}/'
        Comic_Name = Comic_Link.split("/")[-1].replace('%20', " ")
        if os.name == "posix":
            try:
                for Loop in range(1, int(Default_Loop_Value)):
                    Path = Default_Path
                    File_Name = ('{0:0>3}'.format(Loop)) + '.jpg'
                    print(f'Downloading: {"{0:0>3}".format(Loop)}.jpg || Comic Name: {Comic_Name} || Scrapping At: {Comic_Download_Link + "{0:0>3}".format(Loop) + ".jpg"}')
                    with open(File_Name, "wb") as Writer:
                        print(Comic_Download_Link+'{0:0>3}'.format(Loop))
                        Image_Handler = requests.get(url=Comic_Download_Link+'{0:0>3}'.format(Loop)+".jpg", data=random.choice(User_Agent), proxies={f'{Site_Protocol}': f'{Site_Protocol}://{random.choice(Proxies)}'}, timeout=Timeout, stream=True)
                        if Image_Handler.status_code == 503 or Image_Handler.status_code == 520:
                            print("Finished Downloading ;)")
                            exit()
                        Writer.write(Image_Handler.content)
            except (requests.RequestException, requests.ConnectTimeout, requests.ConnectionError):
                print("\n\n\nYou Ate Probably Offline, Please Check Your Internet Connection First The Re-Run This script\nStable Internet Is Required.")
                exit()
        else:
            try:
                for Loop in range(1, int(Default_Loop_Value)):
                    Path = Default_Path
                    File_Name = ('{0:0>3}'.format(Loop)) + '.jpg'
                    print(f'Downloading: {"{0:0>3}".format(Loop)}.jpg || Comic Name: {Comic_Name} || Scrapping At: {Comic_Download_Link + "{0:0>3}".format(Loop) + ".jpg"}')
                    with open(File_Name, "wb") as Writer:
                        Image_Handler = requests.get(url=Comic_Download_Link+'{0:0>3}'.format(Loop)+".jpg", data=random.choice(User_Agent), proxies={f'{Site_Protocol}': f'{Site_Protocol}://{random.choice(Proxies)}'}, timeout=Timeout, stream=True)
                        if Image_Handler.status_code == 503 or Image_Handler.status_code == 520:
                            print("Finished Downloading ;)")

                            exit()
                        Writer.write(Image_Handler.content)
            except (requests.RequestException, requests.ConnectTimeout, requests.ConnectionError):
                print("\n\n\nYou Ate Probably Offline, Please Check Your Internet Connection First The Re-Run This script\nStable Internet Is Required.")
                exit()
    Downloader()


if __name__ == "__main__":
    def Check_For_Required_Files_If_Exist():
        if os.path.isdir("Comic Folder"):
            pass
        else:
            os.mkdir("Comic Folder")
        if os.path.isfile(".Settings.yaml"):
            pass
        else:
            with open(".Settings.yaml", "w") as Writer:
                Writer.write("""# Only modify what you know to avoid errors!!!


Settings:

  Script_Override:
    Default_Loop_Value: 999   # Default value: "999"
    Site_Protocol: http  # Default value: "http"
    Script_Password: ""  # Adding any value inside these quotations will be your password. Leave it empty if you don't want it.
    Default_Path: Comic Folder

  Website_Data:   # Required data for requests packages
    Static_Yiff_Link: https://static.yiffer.xyz/comics/
    Timeout: 5   # In seconds

  Website_Ping_Data:   # What website to check user's internet connection status
    Ping: https://google.com

  Fake_Credentials:  # To avoid ip blocking caused by the ddos protection provider
    Proxies:
      - 95.80.98.41:8080
      - 95.141.36.112:8686
      - 94.140.208.226:8080
      - 91.240.97.69:1080
      - 91.240.97.69:8080
      - 94.247.244.106:3128
      - 89.248.244.182:8080
      - 88.247.10.31:8080
      - 79.104.25.218:8080
      - 78.11.85.10:8080
      - 77.237.121.22:8080
      - 77.120.137.143:8080
      - 78.81.245.153:8080
      - 77.38.21.239:8080
      - 62.213.14.166:8080
      - 65.182.5.212:8080
      - 61.19.27.201:8080
      - 61.19.145.66:8080
      - 62.201.217.194:8080
      - 50.246.120.125:8080
      - 50.201.51.216:8080
      - 51.91.109.83:80
      - 49.0.39.186:8080
      - 46.101.215.222:8118
      - 45.250.226.14:3128
      - 45.250.226.14:8080
      - 45.114.38.25:8080
      - 45.114.36.33:8080
      - 45.172.108.48:9991
      - 43.227.129.65:81
      - 43.245.216.178:8080
      - 45.172.108.50:9991
      - 43.250.127.98:9001
      - 41.65.146.38:8080
      - 45.117.77.41:80
      - 41.204.87.90:8080
      - 41.220.114.154:8080
      - 36.92.116.26:8080
      - 41.60.216.148:8080
      - 36.92.22.70:8080
      - 36.92.107.194:8080
      - 36.67.198.35:3128
      - 36.91.194.25:8080
      - 31.131.67.14:8080
      - 27.116.51.115:8080
      - 27.147.210.35:8080
      - 27.72.244.228:8080
      - 27.254.149.139:80
      - 217.19.209.253:8080
      - 212.92.204.54:8080
      - 217.196.20.150:8080
      - 212.92.204.54:80
      - 212.46.255.78:8080
      - 212.73.73.234:8081
      - 212.156.55.34:8080
      - 213.168.210.76:80
      - 212.200.27.134:8080
      - 203.192.199.114:8080
      - 203.192.217.11:8080
      - 202.57.2.19:8080
      - 202.80.231.67:8080
      - 203.142.74.171:8888
      - 202.154.190.234:8080
      - 202.142.158.114:8080
      - 202.152.24.50:8080
      - 203.76.124.35:8080
      - 202.165.47.26:8080
      - 203.150.172.151:8080
      - 202.134.191.156:8080
      - 202.162.214.250:8080
      - 200.54.247.98:8080
      - 200.199.38.234:8080
      - 200.216.182.118:8080
      - 200.141.248.186:8080
      - 200.149.24.194:8080
      - 200.188.151.212:8080
      - 200.37.231.66:8080
      - 198.229.231.13:8080
      - 197.221.89.70:8080
      - 200.147.153.131:80
      - 192.99.160.45:8080
      - 195.178.56.37:8080
      - 195.24.53.195:80
      - 193.86.229.230:8080
      - 191.242.230.135:8080
      - 195.178.56.33:8080
      - 195.98.79.117:8080
      - 193.150.117.5:8000
      - 190.145.154.214:80
      - 189.80.63.50:8080
      - 189.80.135.130:8080
      - 189.39.127.118:8080
      - 190.214.27.46:8080
      - 190.122.186.229:8080
      - 187.95.125.71:3128
      - 187.44.1.167:8080
      - 189.11.248.162:8080
      - 186.227.119.207:6699
      - 187.11.216.80:8080
      - 187.95.114.125:3128
      - 189.80.3.187:8080
      - 186.233.104.164:8080
      - 186.225.157.22:8080
      - 185.48.149.60:8080
      - 187.6.108.42:8080
      - 185.128.104.33:8080
      - 185.23.128.180:3128
      - 185.21.67.212:80
      - 185.128.104.117:8080
      - 185.189.211.70:8080
      - 183.88.237.226:8080
      - 182.253.60.170:8083
      - 182.23.107.210:3128
      - 182.52.229.165:8080
      - 181.188.166.82:8080
      - 182.253.66.206:3128
      - 180.189.168.66:3129
      - 181.188.166.74:8080
      - 179.43.96.178:8080
      - 178.66.182.76:3128
      - 178.250.92.18:8080
      - 178.217.140.70:443
      - 177.99.206.82:8080
      - 177.130.140.80:8080
      - 176.115.197.118:8080
      - 177.124.184.52:8080
      - 176.235.99.13:9090
      - 167.71.190.253:80
      - 170.231.187.209:8091
      - 164.115.22.45:8080
      - 170.233.235.249:3128
      - 152.169.106.145:8080
      - 154.0.155.205:8080
      - 150.129.201.30:6666
      - 143.255.142.80:8080
      - 150.129.171.123:6666
      - 149.54.10.226:8080
      - 139.255.89.242:8080
      - 151.80.65.175:3128
      - 14.225.5.68:80
      - 139.5.132.245:8080
      - 139.255.25.106:8080
      - 134.249.156.228:82
      - 136.243.81.120:80
      - 134.0.63.134:8000
      - 125.62.198.97:83
      - 125.25.82.191:8080
      - 139.255.31.26:8080
      - 125.62.194.33:83
      - 125.62.193.17:83
      - 125.62.214.161:82
      - 125.62.213.161:83
      - 125.25.206.28:8080
      - 125.62.193.209:83
      - 124.158.175.19:8080
      - 123.1.170.138:3128
      - 119.110.209.94:3128
      - 119.15.89.106:8080
      - 118.67.219.153:8080
      - 118.175.244.111:8080
      - 115.85.65.94:8080
      - 117.102.78.42:8080
      - 116.68.160.114:8080
      - 115.249.2.192:8080
      - 115.124.64.234:8080
      - 111.68.26.237:8080
      - 109.170.97.146:8085
      - 109.201.9.99:8080
      - 107.178.6.30:8080
      - 109.167.141.137:8080
      - 103.95.40.211:3128
      - 103.76.175.88:8080
      - 105.112.8.53:3128
      - 103.9.188.72:443
      - 103.28.121.58:80
      - 103.28.121.58:3128
      - 103.250.157.43:6666
      - 103.209.131.3:8080
      - 103.252.163.191:80
      - 103.250.153.203:8080
      - 103.78.141.27:8080
      - 103.26.54.94:8080
      - 103.253.113.54:80
      - 103.252.117.100:8080
      - 103.28.121.58:80
      - 103.15.60.23:8080
      - 190.151.94.3:46615
      - 103.106.114.134:8080
      - 103.111.55.58:1931
      - 103.101.17.172:8080
      - 103.101.233.13:8080
      - 200.122.86.177:8080
      - 114.34.234.201:3128
      - 103.123.64.234:3128
      - 103.9.188.229:36984
      - 1.10.188.140:43327
      - 134.249.167.184:53281
      - 181.52.85.249:36107
      - 1.2.169.49:36335
      - 94.140.208.226:8080
      - 95.217.34.209:3128
      - 202.75.97.82:47009
      - 122.2.28.114:8080
      - 176.235.99.13:9090
      - 173.46.67.172:58517
      - 177.220.188.213:8080
      - 84.201.254.47:3128
      - 181.209.97.42:999
      - 77.38.21.239:8080
      - 181.196.254.202:53281
      - 77.237.121.19:8080
      - 139.255.25.84:3128
      - 178.219.163.231:8888
      - 170.233.235.249:3128
      - 110.172.160.42:44047
      - 77.237.121.22:8080
      - 125.25.206.28:8080
      - 139.255.25.106:8080
      - 202.62.84.210:53281
      - 109.201.9.99:8080
      - 45.112.57.230:61222
      - 103.9.188.72:443
      - 103.92.213.253:43399
      - 223.27.194.66:63141
      - 217.150.77.31:53281
      - 181.143.73.34:53281
      - 49.156.42.210:8080
      - 118.97.100.83:35220
      - 177.184.139.81:38459
      - 200.60.79.11:53281
      - 80.106.247.145:53410
      - 191.242.230.135:8080
      - 160.202.40.20:55655
      - 103.47.67.115:8080
      - 78.8.189.1:32040
      - 50.233.42.98:51696
      - 200.215.171.238:8080
      - 200.38.19.235:80
      - 201.144.14.229:53281
      - 185.21.67.212:80
      - 103.206.254.170:65103
      - 203.207.52.206:8085
      - 154.0.15.166:46547
      - 189.45.199.37:20183
      - 1.10.186.35:37235
      - 201.143.32.82:80
      - 103.123.231.202:3128
      - 115.74.213.139:8080
      - 89.238.255.34:8082
      - 14.102.152.157:8080
      - 212.43.123.18:41258
      - 89.237.29.198:8080
      - 200.38.19.233:80
      - 96.9.69.164:53281
      - 201.149.101.255:8085
      - 14.102.152.158:8080
      - 119.82.253.24:44060
      - 200.38.19.238:80
      - 202.57.2.19:8080
      - 62.213.14.166:8080
      - 103.25.47.130:8080
      - 95.78.174.219:60473
      - 200.115.53.193:3128
      - 103.114.53.2:8080
      - 182.75.202.226:8080
      - 217.175.35.72:3128
      - 103.47.64.85:8080
      - 94.180.249.187:38051
      - 27.72.244.228:8080
      - 158.140.167.148:53281
      - 50.233.228.147:8080
      - 37.247.209.179:8080
      - 134.0.63.134:8000
      - 103.47.67.116:8080
      - 83.175.166.234:8080
      - 85.159.48.170:40014
      - 91.187.113.205:53281
      - 186.47.82.6:41430
      - 114.110.21.50:50464
      - 103.219.162.126:8080
      - 185.131.62.250:53281
      - 103.28.86.241:61954
      - 41.63.170.142:8080
      - 103.78.23.26:80
      - 84.204.40.155:8080
      - 103.250.166.17:6666
      - 78.110.154.177:59888
      - 45.230.8.20:51200
      - 103.199.159.225:40049
      - 222.124.193.113:8080
      - 122.154.66.193:8080
      - 103.232.67.132:8080
      - 179.43.96.178:8080
      - 181.114.224.177:8080
      - 37.120.192.154:8080
      - 203.76.124.35:8080
      - 46.151.145.4:53281
      - 187.16.43.242:38278
      - 159.192.104.53:8080
      - 24.172.82.94:53281
      - 81.95.131.10:44292
      - 184.82.128.211:8080
      - 181.39.48.2:80
      - 113.161.207.99:60626
      - 195.138.83.218:53281
      - 191.5.0.79:53281
      - 103.213.116.195:8080
      - 62.152.75.110:50287
      - 96.9.67.84:8080
      - 196.0.111.194:34638
      - 89.248.244.182:8080
      - 96.9.77.71:8080
      - 202.142.158.114:8080
      - 103.14.198.129:83
      - 193.242.177.105:53281
      - 203.81.95.42:8080
      - 139.255.58.94:8080
      - 213.142.218.226:40816
      - 150.107.207.137:61954
      - 49.156.35.22:8080
      - 45.173.4.190:999
      - 152.231.25.114:8080
      - 186.159.3.41:30334
      - 191.102.125.245:8080
      - 103.70.79.2:8080
      - 93.91.112.247:41258
      - 150.129.52.74:6666
      - 125.163.161.250:8080
      - 142.165.167.117:53281
      - 195.24.53.195:8080
      - 103.26.54.94:8080
      - 103.81.114.182:53281
      - 79.101.98.2:53281
      - 103.70.79.3:8080
      - 177.37.240.52:8080
      - 202.69.38.82:8080
      - 187.45.127.87:20183
      - 187.73.68.14:53281
      - 41.33.179.195:8080
      - 103.101.17.171:8080
      - 36.92.116.26:8080
      - 177.99.206.82:8080

    User_Agents:
      - Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
      - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36
      - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36
      - Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0
      - Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0
      - Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F
      - Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36
      - Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14
      - Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4
      - Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
      - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36""")
                Writer.close()
        Main()
    Clear_Terminal()
    print("Loading Please Wait...")
    Check_For_Required_Files_If_Exist()

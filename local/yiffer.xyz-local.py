from tokenize import Imagnumber
import requests
import shutil 

yiffLink = 'https://yiffer.xyz/Rainbow%20Dash'            ################################
comicName = yiffLink.split("/")[-1]                       #                              #
staticYiffLink = "https://static.yiffer.xyz/comics"       # edit these lines as seen fit #
path = "comic folder/"                                    #                              #
                                                          ################################




print(yiffLink, '\n', comicName)

for i in range(1,999):
    print('running')
    fileName = str(i)
    length = len(fileName)
    print("length: ", length)
    if length == 1:
        fileName = '0'+'0'+ fileName
    elif length == 2:
        fileName = '0' + fileName
    elif length == 0: break #break if error 
    fileName += '.jpg'


    print(staticYiffLink + '/' + comicName + '/' + fileName)
    imageBuffer = requests.get((staticYiffLink + '/' + comicName + '/' + fileName), stream = True)
    imageBuffer.raw.decode_content = True
    if imageBuffer.status_code == 200:
        with open(path + fileName,'wb') as f:
            shutil.copyfileobj(imageBuffer.raw, f)
        print("done downloading ", testint)
    if imageBuffer.status_code == 404:                                #breaks when execution completes
        break

print("execution complete")





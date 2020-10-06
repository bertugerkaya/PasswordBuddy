from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

print('''

█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▄▄ █░█ █▀▄ █▀▄ █▄█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ █▄█ █▄▀ █▄▀ ░█░
              Cʜᴀɴɢᴇ Pᴀssᴡᴏʀᴅs Qᴜɪᴄᴋʟʏ


Cʜᴏᴏsᴇ ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ! / Dɪʟ Sᴇᴄɪɴɪᴢ!
1) Eɴɢʟɪsʜ
2) Tᴜʀᴋᴄᴇ


''')

language = input(str("Choice / Secim: "))
time.sleep(1)


print('''

█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▄▄ █░█ █▀▄ █▀▄ █▄█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ █▄█ █▄▀ █▄▀ ░█░
              Cʜᴀɴɢᴇ Pᴀssᴡᴏʀᴅs Qᴜɪᴄᴋʟʏ


Cʜᴏᴏsᴇ ᴛʜᴇ Pʟᴀᴛғᴏʀᴍ:
1) Iɴsᴛᴀɢʀᴀᴍ
2) Fᴀᴄᴇʙᴏᴏᴋ
3) Gɪᴛʜᴜʙ 
4) Gᴍᴀɪʟ (Sᴏᴏɴ!)
5) Tᴡɪᴛᴛᴇʀ (Sᴏᴏɴ!)

''')
time.sleep(1)

if language =="1":
    platform = input(str("Choose the Platform: "))
    if platform=="1":
        time.sleep(1)
        userid = input(str('Your Username: '))
        userpwd = input(str('Your Password: '))
        usernew = input(str('Your new Password: '))
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Started! ")
        time.sleep(1)

        path = 'C:\\Users\\kral_\\OneDrive\\Masaüstü\\path\\geckodriver.exe'
        browser = webdriver.Firefox(executable_path=path)


        browser.get('https://www.instragram.com/')
        time.sleep(5)
        username = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/label[1]/input[1]")
        passw = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
        username.send_keys(userpwd)
        passw.send_keys(userid)
        time.sleep(3)
        signin = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]").click()
        time.sleep(5)
        tosettings = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/span[1]/img[1]").click()
        time.sleep(1)
        insettings = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div[2]/div[2]/a[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(3)
        changepw = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[2]/a").click()
        time.sleep(3)
        oldpw = browser.find_element_by_xpath("//input[@id='cppOldPassword']")
        oldpw.send_keys(userpwd)
        newpwd = browser.find_element_by_xpath("//input[@id='cppNewPassword']")
        newpwd.send_keys(usernew)
        confirm = browser.find_element_by_xpath("//input[@id='cppConfirmPassword']")
        confirm.send_keys(usernew)
        time.sleep(2)
        confirmall = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/div/button").click()
        time.sleep(2)
        tologout = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/span[1]/img[1]").click()
        time.sleep(2)
        logout = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[3]/div/div[2]/div/div/div").click()
        time.sleep(2)
        browser.quit
        print("Your Password has been changed succesfully! ")
    elif platform=="2":
        fbuserid = input('Your E-Mail Address: ')
        fbuserpwd = input('Your Password: ')
        fbusernew = input('Your New Password: ')
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Started! ")

        path = 'C:\\Users\\kral_\\OneDrive\\Masaüstü\\path\\geckodriver.exe'
        browser = webdriver.Firefox(executable_path=path)


        browser.get('https://www.facebook.com/')
        time.sleep(5)
        fbuser = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
        fbuser.send_keys(fbuserid)
        time.sleep(1)
        fbpwd = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input")
        fbpwd.send_keys(fbuserpwd)
        time.sleep(2)
        fblogin = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(5)
        fbset = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/a/div").click()
        time.sleep(1)
        fbinset = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div/div[1]/div/div/ul/li[7]/a/span/span").click()
        time.sleep(5)
        fbinpw = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/ul/li[2]/a/div[2]/div").click()
        time.sleep(1)
        fbpw = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/table/tbody/tr/td[3]/button").click()
        time.sleep(1)
        fbpwold = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[1]/table/tbody/tr[3]/td/input")
        fbpwold.send_keys(fbuserpwd)
        time.sleep(1)
        fbpwnew = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[1]/table/tbody/tr[5]/td/input")
        fbpwnew.send_keys(fbusernew)
        time.sleep(1)
        fbpwnewconfirm = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[1]/table/tbody/tr[7]/td/input")
        fbpwnewconfirm.send_keys(fbusernew)
        time.sleep(1)
        fbpwdone = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[2]/div/label/input").click()
        time.sleep(1)
        fblogout = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/a/div").click()
        time.sleep(1)
        fblogoutdone = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div").click()
        browser.quit
        print("Your Password has been changed succesfully! ")
    elif platform=="3":
        gtuserid = input('Your Username: ')
        gtuserpwd = input('Your Password: ')
        gtusernew = input('Your New Password: ')
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Started! ")
        
        path = 'C:\\Users\\kral_\\OneDrive\\Masaüstü\\path\\geckodriver.exe'
        browser = webdriver.Firefox(executable_path=path)


        browser.get('https://www.github.com/login')
        time.sleep(3)
        gtuser = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")
        gtuser.send_keys(gtuserid)
        time.sleep(1)
        gtpwd = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")
        gtpwd.send_keys(gtuserpwd)
        time.sleep(1)
        gtlogin = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]").click()
        time.sleep(3)
        browser.get("https://github.com/settings/security")
        time.sleep(3)
        gtold = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/dl/dd/input")
        gtold.send_keys(gtuserpwd)
        time.sleep(1)
        gtnew = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/password-strength/dl[1]/dd/auto-check/input[1]")
        gtnew.send_keys(gtusernew)
        time.sleep(1)
        gtnewconfirm = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/password-strength/dl[2]/dd/input")
        gtnewconfirm.send_keys(gtusernew)
        time.sleep(1)
        gtfin = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/p/button").click()
        time.sleep(3)
        browser.get("https://github.com/logout")
        gtlogout = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/input[2]").click()
        browser.quit
        print("Your Password has been changed succesfully! ")


    else:
        print(str("You made a wrong choice! "))
    
elif language=="2":
    platform = input(str("Platform Seçiniz: "))
    if platform=="1":
        time.sleep(1)
        userid = input(str('Kullanıcı adını giriniz: '))
        userpwd = input(str('Şifrenizi Giriniz: '))
        usernew = input(str('Yeni Sifrenizi Giriniz: '))
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Işlem Başladı! ")
        time.sleep(1)

        path = 'C:\\Users\\kral_\\OneDrive\\Masaüstü\\path\\geckodriver.exe'
        browser = webdriver.Firefox(executable_path=path)


        browser.get('https://www.instragram.com/')
        time.sleep(5)
        username = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/label[1]/input[1]")
        passw = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
        username.send_keys(userpwd)
        passw.send_keys(userid)
        time.sleep(3)
        signin = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]").click()
        time.sleep(5)
        tosettings = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/span[1]/img[1]").click()
        time.sleep(1)
        insettings = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div[2]/div[2]/a[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(3)
        changepw = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[2]/a").click()
        time.sleep(3)
        oldpw = browser.find_element_by_xpath("//input[@id='cppOldPassword']")
        oldpw.send_keys(userpwd)
        newpwd = browser.find_element_by_xpath("//input[@id='cppNewPassword']")
        newpwd.send_keys(usernew)
        confirm = browser.find_element_by_xpath("//input[@id='cppConfirmPassword']")
        confirm.send_keys(usernew)
        time.sleep(2)
        confirmall = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/div/button").click()
        time.sleep(2)
        tologout = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/span[1]/img[1]").click()
        time.sleep(2)
        logout = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[3]/div/div[2]/div/div/div").click()
        time.sleep(2)
        browser.quit
        print("Şifreniz Başarıyla Değiştirildi! ")
    elif platform=="2":
        fbuserid = input('E-Mail adresinizi giriniz: ')
        fbuserpwd = input('Şifrenizi Giriniz: ')
        fbusernew = input('Yeni Sifrenizi Giriniz: ')
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Işlem Başladı! ")

        path = 'C:\\Users\\kral_\\OneDrive\\Masaüstü\\path\\geckodriver.exe'
        browser = webdriver.Firefox(executable_path=path)


        browser.get('https://www.facebook.com/')
        time.sleep(5)
        fbuser = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
        fbuser.send_keys(fbuserid)
        time.sleep(1)
        fbpwd = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input")
        fbpwd.send_keys(fbuserpwd)
        time.sleep(2)
        fblogin = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(5)
        fbset = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/a/div").click()
        time.sleep(1)
        fbinset = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div/div[1]/div/div/ul/li[7]/a/span/span").click()
        time.sleep(5)
        fbinpw = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/ul/li[2]/a/div[2]/div").click()
        time.sleep(1)
        fbpw = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/table/tbody/tr/td[3]/button").click()
        time.sleep(1)
        fbpwold = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[1]/table/tbody/tr[3]/td/input")
        fbpwold.send_keys(fbuserpwd)
        time.sleep(1)
        fbpwnew = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[1]/table/tbody/tr[5]/td/input")
        fbpwnew.send_keys(fbusernew)
        time.sleep(1)
        fbpwnewconfirm = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[1]/table/tbody/tr[7]/td/input")
        fbpwnewconfirm.send_keys(fbusernew)
        time.sleep(1)
        fbpwdone = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div/form/div/div[2]/div/label/input").click()
        time.sleep(1)
        fblogout = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/a/div").click()
        time.sleep(1)
        fblogoutdone = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div").click()
        browser.quit
        print("Şifreniz Başarıyla Değiştirildi! ")
    elif platform=="3":
        gtuserid = input('Kullanıcı adınızı giriniz: ')
        gtuserpwd = input('Şifrenizi Giriniz: ')
        gtusernew = input('Yeni Sifrenizi Giriniz: ')
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Işlem Başladı! ")
        
        path = 'C:\\Users\\kral_\\OneDrive\\Masaüstü\\path\\geckodriver.exe'
        browser = webdriver.Firefox(executable_path=path)


        gtuserid = input('Kullanıcı adınızı giriniz: ')
        gtuserpwd = input('Şifrenizi Giriniz: ')
        gtusernew = input('Yeni Sifrenizi Giriniz: ')
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Işlem Başladı! ")
        
        path = 'C:\\Users\\kral_\\OneDrive\\Masaüstü\\path\\geckodriver.exe'
        browser = webdriver.Firefox(executable_path=path)


        browser.get('https://www.github.com/login')
        time.sleep(3)
        gtuser = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")
        gtuser.send_keys(gtuserid)
        time.sleep(1)
        gtpwd = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")
        gtpwd.send_keys(gtuserpwd)
        time.sleep(1)
        gtlogin = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]").click()
        time.sleep(3)
        browser.get("https://github.com/settings/security")
        time.sleep(3)
        gtold = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/dl/dd/input")
        gtold.send_keys(gtuserpwd)
        time.sleep(1)
        gtnew = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/password-strength/dl[1]/dd/auto-check/input[1]")
        gtnew.send_keys(gtusernew)
        time.sleep(1)
        gtnewconfirm = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/password-strength/dl[2]/dd/input")
        gtnewconfirm.send_keys(gtusernew)
        time.sleep(1)
        gtfin = browser.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/form/p/button").click()
        time.sleep(3)
        browser.get("https://github.com/logout")
        gtlogout = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/input[2]").click()
        browser.quit
        print("Şifreniz Başarıyla Değiştirildi! ")

    else:
        print(str("Hatalı Seçim Yaptınız! "))
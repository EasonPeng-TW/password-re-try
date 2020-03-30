
count = 0
while True:
    count = count + 1
    pw = input('請輸入你的密碼: ')
    if pw == '123':
        print('密碼正確')
        break
    else:
        print('您輸入的密碼有誤, 錯誤第', count, '次')
        if count == 3:
            print('輸入次數已達上限，您的帳戶將遭鎖定')
            break

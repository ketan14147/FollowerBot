from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from random import randint, choice

class AddMeFast:
    def setup(self):
        Setup.init(self)
        sleep(4)
        self.browser.get('https://addmefast.com')
        sleep(4)
        username = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[1]')
        username.send_keys(YOUR ADDMEFAST E-MAIL ADDRESS)

        password = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[2]')
        password.send_keys('YOUR ADDMEFAST PASSWORD)

        button = self.browser.find_element(By.NAME, 'login_button')
        button.click()
        sleep(6)

        if "Login" in self.browser.page_source:
            print('Something went wrong in Addmefast login process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Logged in AddmeFast. Your current point is: ' + point.text)

    def login_gmail(self):
        self.browser.get('https://mail.google.com')
        sleep(5)

        actions = ActionChains(self.browser)
        actions.send_keys(YOUR GMAIL ADDRESS).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(2)

        actions.send_keys(YOUR GMAIL PASSWORD).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()

        sleep(10)
        if "Log In" in self.browser.page_source:
            print('Something went wrong in Gmail login process.')
        else:
            print('Logged in Gmail.')

    def login_facebook(self):
        self.browser.get('https://www.facebook.com/')
        sleep(15)

        cookies = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_9xo5'))
        )
        cookies.click()
        sleep(5)

        username = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        username.send_keys(YOUR FACEBOOK E-MAIL ADDRESS)

        password = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "pass"))
        )
        password.send_keys(YOUR FACEBOOK PASSWORD)
        sleep(2)

        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)
        if "Log In" in self.browser.page_source:
            print('Something went wrong in Facebook login process.')
        else:
            print('Logged in Facebook.')

    def login_twitter(self):
        self.browser.get('https://twitter.com/i/flow/login')

        N = 4
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        sleep(3)
        actions.send_keys(YOUR TWITTER USERNAME).perform()
        sleep(2)

        actions.send_keys(Keys.RETURN).perform()
        sleep(2)

        actions.send_keys(YOUR TWITTER PASSWORD).perform()
        sleep(2)

        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        M = 2
        for _ in range(M):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)
        if "Log in" in self.browser.page_source:
            print('Something went wrong in Twitter login process.')
        else:
            print('Logged in Twitter.')

    def login_instagram(self):
        self.browser.get('https://www.instagram.com/')
        sleep(5)

        cookies = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Only allow essential cookies')]"))
        )
        cookies.click()
        sleep(5)

        N = 2
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions = actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        username = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys(YOUR INSTAGRAM USERNAME)

        password = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password.send_keys(YOUR INSTAGRAM PASSWORD)
        sleep(2)

        actions.send_keys(Keys.RETURN).perform()
        sleep(10)
        if "Log in" in self.browser.page_source:
            print('Something went wrong in Instagram login process.')
        else:
            print('Logged in Instagram.')

    def login_reddit(self):
        self.browser.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

        username = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username.send_keys(YOUR REDDIT USERNAME)
        sleep(2)

        password = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password.send_keys(YOUR REDDIT PASSWORD)
        sleep(2)

        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)

        if "LOG IN" in self.browser.page_source:
            print('Something went wrong in Reddit login process.')
        else:
            print('Logged in Reddit.')

    def login_pinterest(self):
        self.browser.get('https://www.pinterest.com/')
        sleep(4)

        N = 6
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions = actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        actions.send_keys(YOUR PINTEREST E-MAIL ADDRESS).perform()
        sleep(2)
        actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(YOUR PINTEREST PASSWORD).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)

        if "Log In" in self.browser.page_source:
            print('Something went wrong in Pinterest login process.')
        else:
            print('Logged in Pinterest.')

    def surf_website(self):
        self.browser.get('https://addmefast.com/websites')
        sleep(25)
        if EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'No items')]")):
            print('Something went wrong in web surfing process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Web surfing process is successful. Your point is: ' + point.text)

    def youtube_view(self):
        self.browser.get('https://addmefast.com/free_points/youtube_views')
        sleep(4)
        watch = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "View Video"))
        )
        watch.click()
        WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/strong[2]'))
        )
        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Youtube view process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Youtube view process is successful. Your point is: ' + point.text)

    def instagram_like(self):
        self.browser.get('https://addmefast.com/free_points/instagram_likes')
        sleep(4)
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
        )
        like.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        N = 11
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(2)
        actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Instagram like process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Instagram like process is successful. Your point is: ' + point.text)

    def instagram_follow(self):
        self.browser.get('https://addmefast.com/free_points/instagram')
        sleep(4)
        follow = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        follow.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        do_follow = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]"))
        )
        do_follow.click()
        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Instagram follow process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Instagram follow process is successful. Your point is: ' + point.text)

    def twitter_follow(self):
        self.browser.get('https://addmefast.com/free_points/twitter')
        sleep(4)
        follow = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        follow.click()
        sleep(10)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Twitter follow process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Twitter follow process is successful. Your point is: ' + point.text)

    def twitter_like(self):
        self.browser.get('https://addmefast.com/free_points/twitter_likes')
        sleep(4)
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
        )
        like.click()
        sleep(10)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Twitter like process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Twitter like process is successful. Your point is: ' + point.text)

    def twitter_retweet(self):
        self.browser.get('https://addmefast.com/free_points/twitter_retweets')
        sleep(4)
        retweet = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Retweet"))
        )
        retweet.click()
        sleep(10)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Twitter retweet process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Twitter retweet process is successful. Your point is: ' + point.text)

    def facebook_followers(self):
        self.browser.get('https://addmefast.com/free_points/facebook_subscribes')
        sleep(4)
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        like.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        N = 16
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(15)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Facebook follower process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Facebook followers process is successful. Your point is: ' + point.text)

    def facebook_share(self):
        self.browser.get('https://addmefast.com/free_points/facebook_share')
        sleep(4)
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Share"))
        )
        like.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        N = 8
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(2)
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(15)

        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Facebook share process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Facebook share process is successful. Your point is: ' + point.text)

    def reddit_members(self):
        self.browser.get('https://addmefast.com/free_points/reddit_members')
        sleep(4)
        join = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Join"))
        )
        join.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_join = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Join')]"))
        )
        do_join.click()
        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Reddit members process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Reddit members process is successful. Your point is: ' + point.text)

    def youtube_subscribe(self):
        self.browser.get('https://addmefast.com/free_points/youtube_subscribe')
        sleep(4)
        subscribe = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Subscribe"))
        )
        subscribe.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        N = 9
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()

        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Youtube subscribe process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Youtube subscribe process is successful. Your point is: ' + point.text)

    def pinterest_save(self):
        self.browser.get('https://addmefast.com/free_points/pinterest_save')
        sleep(4)
        save = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Save"))
        )
        save.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_save = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save')]"))
        )
        do_save.click()

        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Pinterest save process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Pinterest save process is successful. Your point is: ' + point.text)

    def pinterest_followers(self):
        self.browser.get('https://addmefast.com/free_points/pinterest')
        sleep(4)
        follow = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        follow.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_follow = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]"))
        )
        do_follow.click()

        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        if "Oops!" in self.browser.page_source:
            print('Something went wrong in Pinterest follow process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Pinterest follow process is successful. Your point is: ' + point.text)

    def close_browser(self):
        Setup.close_browser(self)

amf = AddMeFast()
amf.setup()
amf.login_facebook()
amf.login_gmail()
amf.login_instagram()
amf.login_pinterest()
amf.login_reddit()
amf.login_twitter()

array = [amf.surf_website, amf.youtube_view, amf.twitter_like, amf.twitter_retweet, amf.twitter_follow,
            amf.instagram_like, amf.instagram_follow, amf.facebook_followers, amf.facebook_share, 
            amf.reddit_members, amf.youtube_subscribe, amf.pinterest_save, amf.pinterest_followers]

while(True):
    try:
        choice(array)()
    except:
        delay = randint(100, 300)
        print('We could not find a content to collect points. We are waiting ' + str(delay) + ' seconds...')
        sleep(delay)

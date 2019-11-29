# 2019.11.24 滑块的验证逻辑貌似需要修改
# 无头模式下暂不支持

import asyncio
import random
import time
from pyppeteer import launcher
from retrying import retry  # 设置重试次数用的

# launcher.AUTOMATION_ARGS.remove("--enable-automation")
from pyppeteer.launcher import launch
from name_pwd import *


def screen_size():
    '使用tkinter获取屏幕大小'
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    print(width, height)
    return width, height


width, height = 1366, 768


async def main(username, pwd, url):  # 定义main协程函数，
    # 以下使用await 可以针对耗时的操作进行挂起
    browser = await launch({
        'args': [
            '--no-sandbox', '--disable-infobars',
            f'--window-size={width},{height}',
            # f'--enable-automation'
        ],
        # 'excludeSwitches': [f'--enable-automation'],
        # 'ignoreDefaultArgs': ["--enable-automation"],
        'headless': False,
        # 'userDataDir': './userdata',  # 是否将页面请求记录保存下来
    })
    # 改变屏幕显示大小
    page = await browser.newPage()  # 启动个新的浏览器页面
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    await page.setViewport({'width': width, 'height': height})

    # await page.goto(url)  # 访问登录页面
    # 替换淘宝在检测浏览时采集的一些参数。
    # 就是在浏览器运行的时候，始终让window.navigator.webdriver=false
    # navigator是windiw对象的一个属性，同时修改plugins，languages，navigator 且让
    # js = """
    #   function sniffDetector() {
    #   const userAgent = window.navigator.userAgent;
    #   const platform = window.navigator.platform;
    #
    #   window.navigator.__defineGetter__('userAgent', function() {
    #     window.navigator.sniffed = true;
    #     return userAgent;
    #   });
    #
    #   window.navigator.__defineGetter__('platform', function() {
    #     window.navigator.sniffed = true;
    #     return platform;
    #   });
    #   //自动化反反爬虫，反自动化检测
    #   Object.defineProperty(navigator, 'webdriver', {
    #       get: () => false,
    #   });
    # }
    #   """
    # await page.evaluateOnNewDocument(js)
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    await page.evaluateOnNewDocument('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluateOnNewDocument(
        '''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5, 6], }); }''')
    # await page.evaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, 'plugins', {get: () = > {'userAgent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'},});}''')
    #     await page.evaluateOnNewDocument('''() => {
    #   const originalQuery = window.navigator.permissions.query;
    #   return window.navigator.permissions.query = (parameters) => (
    #     parameters.name === 'notifications' ?
    #       Promise.resolve({ state: Notification.permission }) :
    #       originalQuery(parameters)
    #   );
    # });''')

    # 使用type选定页面元素，并修改其数值，用于输入账号密码，修改的速度仿人类操作，因为有个输入速度的检测机制
    # 因为 pyppeteer 框架需要转换为js操作，而js和python的类型定义不同，所以写法与参数要用字典，类型导入
    # await page.type('.J_UserName', username, {'delay': input_time_random() - 50})
    # await page.type('#J_StandardPwd input', pwd, {'delay': input_time_random()}) Object.defineProperty(navigator, 'plugins', { get: () => {xx:yy}, });
    await page.goto(url)  # 访问登录页面
    # print(browser.userAgent())
    # await page.screenshot({'path': './1.png'})
    await page.evaluate('''document.getElementById("J_Quick2Static").click()''')
    await asyncio.sleep(0.5)
    # await page.screenshot({'path': './2.png'})
    await page.type('#TPL_username_1', username, {'delay': input_time_random() - 50})
    await page.type('#TPL_password_1', pwd, {'delay': input_time_random()})

    # await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')
    # await asyncio.sleep(2)
    # await page.type('#TPL_password_1', pwd, {'delay': random.randint(100, 151)})
    # await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')

    # await page.screenshot({'path': './headless-test-result.png'})    # 截图测试
    # await asyncio.sleep(2)
    # await page.screenshot({'path': './3.png'})
    await asyncio.sleep(2)
    # 检测页面是否有滑块。原理是检测页面元素。
    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块

    if slider:
        print('当前页面出现滑块')
        # await page.type('#TPL_password_1', pwd, {'delay': random.randint(100, 151)})
        # await page.screenshot({'path': './headless-login-slide.png'})  # 截图测试
        flag, page = await mouse_slide(page=page)  # js拉动滑块过去。
        if flag:
            # await page.keyboard.press('Enter')  # 确保内容输入完毕，少数页面会自动完成按钮点击
            print("print enter", flag)
            await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')  # 如果无法通过回车键完成点击，就调用js模拟点击登录按钮。

            time.sleep(2)
            # cookies_list = await page.cookies()
            # print(cookies_list)
            await get_cookie(page)  # 导出cookie 完成登陆后就可以拿着cookie玩各种各样的事情了。
    else:
        print("无滑块，正在验证登陆")
        await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')
        await page.waitFor(20)
        await page.waitForNavigation()
        error = ''
        try:
            print("正在检测是否是账号密码错误")
            error = await page.Jeval('#J_Message > p', 'node => node.textContent')
        except:
            error = None
        finally:
            if error:
                print("error:", error)
                await browser.close()  # 程序退出。
                loop.close()
            else:
                # res = await page.content()
                # print(res)
                # if '密码登录' in res:
                #     raise ValueError('登录失败！')
                # print('登陆后所在页面为：' + page.url)
                # await page.screenshot({'path': './4.png'})
                cookies = await get_cookie(page)
                print(cookies)
                await asyncio.sleep(100)
                await browser.close()


# 获取登录后cookie
async def get_cookie(page):
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1};'
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    return cookies


def retry_if_result_none(result):
    return result is None


@retry(retry_on_result=retry_if_result_none, )
async def mouse_slide(page=None):
    await asyncio.sleep(2)
    try:
        # 鼠标移动到滑块，按下，滑动到头（然后延时处理），松开按键
        await page.hover('#nc_1_n1z')  # 不同场景的验证码模块能名字不同。
        await page.mouse.down()
        await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
        await page.mouse.up()
    except Exception as e:
        print(e, ':验证失败')
        return None, page
    else:
        await asyncio.sleep(2)
        # 判断是否通过
        slider_again = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')
        if slider_again != '验证通过':
            print('验证失败')
            await page.screenshot({'path': './headless-slide-result.png'})
            return None, page
        else:
            # await page.screenshot({'path': './headless-slide-result.png'}) # 截图测试
            print('验证通过')
            return 1, page


def input_time_random():
    return random.randint(100, 151)


if __name__ == '__main__':

    # url = 'https://login.taobao.com/member/login.jhtml?style=mini&css_style=b2b&from=b2b&full_redirect=true&redirect_url=https://login.1688.com/member/jump.htm?target=https://login.1688.com/member/marketSigninJump.htm?Done=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&reg= http://member.1688.com/member/join/enterprise_join.htm?lead=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&leadUrl=http://login.1688.com/member/'
    url = 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3D%25E7%25BE%258E%25E9%25A3%259F%26imgfile%3D%26commend%3Dall%26ssid%3Ds5-e%26search_type%3Ditem%26sourceId%3Dtb.index%26spm%3Da21bo.2017.201856-taobao-item.1%26ie%3Dutf8%26initiative_id%3Dtbindexz_20170306'
    loop = asyncio.get_event_loop()  # 协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    loop.run_until_complete(main(username, pwd, url))

# import asyncio
# import random
# import time
#
# import pyppeteer
#
#
# class LoginTaoBao:
#     """
#     类异步
#     """
#     pyppeteer.DEBUG = True
#     page = None
#
#     async def _injection_js(self):
#         """注入js
#         """
#         await self.page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
#                                               '{webdriver:{ get: () => false } }) }')  # 本页刷新后值不变
#
#     async def _init(self):
#         """初始化浏览器
#         """
#         browser = await pyppeteer.launch({
#             # 'headless': False,
#             # 'userDataDir': './userdata',
#             'args': [
#                 f'--window-size={1366},{768}'
#                 f'--disable-extensions',
#                 f'--hide-scrollbars',
#                 f'--disable-bundled-ppapi-flash',
#                 f'--mute-audio',
#                 f'--no-sandbox',
#                 f'--disable-setuid-sandbox',
#                 f'--disable-gpu',
#                 f'--disable-infobars'
#             ],
#             'dumpio': True
#         })
#         self.page = await browser.newPage()
#         # 设置浏览器头部
#         await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
#         # 设置浏览器大小
#         await self.page.setViewport({'width': 1366, 'height': 768})
#
#     async def get_cookie(self):
#         cookies_list = await self.page.cookies()
#         cookies = ''
#         for cookie in cookies_list:
#             str_cookie = '{0}={1};'
#             str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
#             cookies += str_cookie
#         print(cookies)
#         return cookies
#
#     async def mouse_slider(self):
#         """滑动滑块
#         """
#         await asyncio.sleep(3)
#         try:
#             await self.page.hover('#nc_1_n1z')
#             # 鼠标按下按钮
#             await self.page.mouse.down()
#             # 移动鼠标
#             await self.page.mouse.move(2000, 0, {'steps': 30})
#             # 松开鼠标
#             await self.page.mouse.up()
#             await asyncio.sleep(2)
#         except Exception as e:
#             print(e, '      :错误')
#             return None
#         else:
#             await asyncio.sleep(3)
#             # 获取元素内容
#             slider_again = await self.page.querySelectorEval('.nc-lang-cnt', 'node => node.textContent')
#             if slider_again != '验证通过':
#                 return None
#             else:
#                 print('验证通过')
#                 return True
#
#     async def main(self, username_, pwd_):
#         """登陆
#         """
#         # 初始化浏览器
#         await self._init()
#         # 注入js
#         await self._injection_js()
#         # 打开淘宝登陆页面
#         await self.page.goto('https://login.taobao.com')
#
#         # await self.page.goto('https://www.taobao.com')
#         # time.sleep(1000000)
#         # 点击密码登陆按钮
#         await self.page.click('div.login-switch')
#         time.sleep(random.random() * 2)
#         # 输入用户名
#         await self.page.type('#TPL_username_1', username_, {'delay': random.randint(100, 151) - 50})
#         # 输入密码
#         await self.page.type('#TPL_password_1', pwd_, {'delay': random.randint(100, 151)})
#         time.sleep(random.random() * 2)
#         # 获取滑块元素
#         slider = await self.page.Jeval('#nocaptcha', 'node => node.style')
#         if slider:
#             print('有滑块')
#             # 移动滑块
#             flag = await self.mouse_slider()
#             if not flag:
#                 print('滑动滑块失败')
#                 return None
#             time.sleep(random.random() + 1.5)
#             # 点击登陆
#             print('点击登陆')
#             await self.page.click('#J_SubmitStatic')
#             await asyncio.sleep(1000)
#
#         print('点击登陆')
#         await self.page.keyboard.press('Enter')
#
#         cookies = await self.get_cookie()
#         time.sleep(10000)
#
#
# if __name__ == '__main__':
#     username = '天涯浪子2013101'
#     pwd = 'gzt13387619000'
#     login = LoginTaoBao()
#     loop = asyncio.get_event_loop()
#     task = asyncio.ensure_future(login.main(username, pwd))
#     loop.run_until_complete(task)

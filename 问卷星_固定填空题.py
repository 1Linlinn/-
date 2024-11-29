import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def clear_cookies(driver):
    """
    模拟清除Cookies的功能
    """
    cookies = driver.get_cookies()
    for cookie in cookies:
        driver.delete_cookie(cookie['name'])

def fill_and_submit_form(driver):
    """
    填写表单并提交表单
    """
    start_time = time.time()  # 记录开始时间
    # 获取类似class名为'field ui-field-contain'的元素列表（这里根据实际页面HTML结构调整选择器）
    question_list = driver.find_elements(By.CLASS_NAME, 'field.ui-field-contain')
    if len(question_list) >= 3:
        # 填写姓名
        name_input = question_list[0].find_element(By.TAG_NAME, 'input')
        name_input.send_keys("小明")

        # 填写学号
        student_id_input = question_list[1].find_element(By.TAG_NAME, 'input')
        student_id_input.send_keys("202302000")

        # 填写联系方式
        contact_input = question_list[2].find_element(By.TAG_NAME, 'input')
        contact_input.send_keys("12345679876")

    # 等待1秒确保字段填写后相关状态更新（适当减少等待时间）
    time.sleep(1)
    submit_button = driver.find_element(By.ID, 'ctlNext')
    submit_button.click()
    end_time = time.time()  # 记录结束时间
    print(f"整个表单填写并提交操作耗时: {end_time - start_time} 秒")

if __name__ == "__main__":
    # 创建Chrome浏览器驱动实例
    driver = webdriver.Chrome()

    # 打开目标网页（这里替换为你实际要操作的网页URL）
    driver.get("https://www.wjx.cn/vm/POHcLCZ.aspx#")  # 请将此处替换为实际URL

    # 模拟清除localStorage和sessionStorage（这里只是简单的重置相关状态，不完全等同）
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    clear_cookies(driver)

    # 滚动到页面底部（使用JavaScript执行滚动操作）
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight, left: 0, behavior: 'smooth'});")

    # 填写表单并提交
    fill_and_submit_form(driver)

    # 可以根据后续需求决定是否关闭浏览器，若需要保持浏览器窗口打开查看结果等，可以注释掉下面这行
    driver.quit()
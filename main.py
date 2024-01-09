if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    print(driver.title)

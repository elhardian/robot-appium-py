from appium import webdriver
import os

appium_server = os.environ.get("APPIUM_SERVER", "http://localhost:4732")
platform_version = os.environ.get("PLATFORM_VERSION", "15.5")
app_build_path = os.environ.get("APP_PATH", None)
device_name = os.environ.get("DEVICE_NAME", "iPhone 13 Pro Max")

desired_caps = {
  "platformName": "iOS",
  "appium:platformVersion": f"{platform_version}",
  "appium:app": f"{app_build_path}",
  "appium:deviceName": f"{device_name}",
  "appium:automationName": "XCUITest",
  "appium:autoAcceptAlerts": "true",
  "appium:newCommandTimeout": "300",
  "appium:autoWebView": "true"
}

driver = webdriver.Remote(f"{appium_server}/wd/hub", desired_caps)
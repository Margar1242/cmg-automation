# Table of Content
* [System Requirements](#system-requirements)
* [Installation](#installation)
* [How To Run](#how-to-run)
* [Headless Mode](#headless-mode)
* [Send test report to email](#-send-test-report-to-email)
* [Send test report to slack](#-send-test-report-to-slack)
* [Jenkins Setup](#-jenkins-setup)

# System Requirements:
 - python3 
 - pip3

# Installation
  - Install allure commandline [installation guide](https://docs.qameta.io/allure/#_installing_a_commandline)  
  - Install appium server [installation guide](https://www.browserstack.com/guide/download-and-install-appium)
  - Install the dependencies (It is highly recommended to create isolated environment!)
  ```sh
  python3 -m venv my_env
  source my_env/bin/activate
  pip3 install -r requirements.txt
  ```
### Used Plugins

| Plugin | README |
| ------ | ------ |
| selenium | To manipulate with browser|
| pytest | To run tests |
| pytest-xdist | To support parallel test run |
| webdriver-manager | To support different versions and type of browsers |
| allure-pytest | To integrate allure reporter with pytests |
| pytest-json-report | To generate json reports |


# How to run

####Note
Before running if you are using masOS and need to execute tests on 
safari browser please follow up the [documentation](https://support.accelq.com/hc/en-us/articles/360028346351-Setting-up-Safari-browser-for-automation)
to enable automation on safari browser. After that run your tests.

 ```sh
$ python3 run.py  --browser chrome
 ```

### Run parameters
- ```--env``` - Set the url in which tests will be run  
 -- Default value ```https://www.google.com/```

```sh
python3 run.py --env https://www.google.com/
```
- ```--page``` - run specific class tests  
 -- Supported values ```home```, ```etc```
 -- No default value  
 -- Parameter is optional  
```sh
python3 run.py --page home
```
- ```--run_mode``` - run specific class tests  
 -- Supported values ```save_cookies```, ```delete_cookies```
 -- Default value is ```save_cookies```
 -- Parameter is optional  
```sh
python3 run.py --page home --run_mode delete_cookies
```
- ```--browser``` - specify the browser in which tests will be run, please note that you can specify multiple browsers  
 -- Supported browsers ```chrome``` , ```firefox```, ```safari```, ```edge```  
 -- Default value ```chrome```  
 -- Parameter is optional  
```sh
python3 run.py --browser chrome firefox
```

```sh
python3 run.py --browser chrome
```

- ```--group``` - run specific group tests  
 -- All supported values are listed in ```pytest.ini``` file  
 -- No default value  
 -- Parameter is optional   
```sh
python3 run.py --group assignments
```
- ```--thread_count``` or ```-t``` - run tests in parallel  
 -- Supported int type values   
 -- Supported ```auto``` value to use as many processes as your computer has CPU cores   
 -- Parameter is optional   
```sh
python3 run.py -t 2
```

- ```--throughput``` - simulate internet connection speed  
 -- Supported only for Google Chrome
```sh
python3 run.py --throughput 90
```
- Running on mobile browsers
    - Additional parameters
        - `--platform` - specify the platform iOS or Android
        - `--type` - specify mobile in order to run on mobile
        - `--deviceOs` - specify device os
        - `--device` - specify device name
    - iOS safari
    ```
     python3 run.py --page home --platform iOS --type mobile --deviceOs 14.3 --device "iPhone 12 Pro"
    ``` 
  - Android Chrome
  ```
     python3 run.py --page home --platform Android --type mobile --deviceOs 10 --device "Android Emulator"
    ``` 
- Running on browserStack browsers
    - Before run
        - Set your browserStack username and key in `configs/bs_config.json` file
    - Parameters
        - `--type` - specify the type browser_stack_web or browser_stack_mobile
        ```
      python3 run.py --page home --browser safari --type browser_stack_mobile --platform iOS
      ```
### Headless mode  
Please note that [xvfb](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml) should be installed on your linux machine.  
```$ sudo apt install xvfb```
- ```--headless``` to enable this mode  
- ``--dimensions`` or ```-d``` to change the default dimensions(1920x1080)  
  --You should specify the dimensions in valid format.[(width)x(height)] for example [1920x1080]  

## Analysing results
After test run is completed you can find full results in reports folder.
To open the results run the following command
```buildoutcfg
python3 runner_util/serve_results.py
```
Or add `--results show` argument when running the tests

```buildoutcfg
 python3 run.py --page home --browser chrome --results show
```

After it follow link and open  http://localhost:6677/reports/ with your browser.

![Html Report](docs/html_results/result1.png)  
Click the row based on the browser you ran your tests to see allure results with step and history in that browser.
![Html Report](docs/html_results/allure_results.png)  

## ![Mail](docs/mail/mail.png) Send test report to email  
![Mail Report](docs/mail/mail_report.png)  
By default this option is turned off, you can specify ```to_email``` parameter to turn on this option  
### Parameters:  
- ```--to_email``` to send email report to specified email address  
```sh
$ python3 run.py --to_email someexampleemail@test.com
```
- ```from_email``` specify sender email  
 -- By default it has value  
- ```--password``` specify sender password  
- ```--smtp_host``` specify SMTP host  
- ```--smtp_port``` specify SMTP port  

## ![Slack](docs/slack/slack.png) Send test report to slack  
![Slack Report](docs/slack/slack_report.png)  
Please read how to create [Incoming Webhooks](https://api.slack.com/messaging/webhooks)  
By default this option is turned off, you can specify  
```--send_slack True``` to turn on this option  

### Parameters:
- ```--slack_hook``` specify the [Incoming Webhooks](https://api.slack.com/messaging/webhooks) url  

```sh
$ python3 run.py --send_slack True --slack_hook https://hooks.slack.com/services/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
```


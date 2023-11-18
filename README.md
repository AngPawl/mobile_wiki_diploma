# Demo Project of mobile tests for <a target="_blank" href="https://github.com/wikimedia/apps-android-wikipedia">Wikipedia</a> app

![This is an image](design/images/homepage.png)

### Tech Stack:
<code><img width="5%" title="Python" src="design/icons/python.png"></code>
<code><img width="5%" title="Pytest" src="design/icons/pytest.png"></code>
<code><img width="5%" title="Selene" src="design/icons/selene.png"></code>
<code><img width="5%" title="Selenium" src="design/icons/selenium.png"></code>
<code><img width="5%" title="Appium" src="design/icons/appium.png"></code>
<code><img width="5%" title="Pydantic" src="design/icons/pydantic.png"></code>
<code><img width="5%" title="Poetry" src="design/icons/poetry.png"></code>
<code><img width="5%" title="Browserstack" src="design/icons/bstack.png"></code>
<code><img width="5%" title="Jenkins" src="design/icons/jenkins.png"></code>
<code><img width="5%" title="Allure-report" src="design/icons/allure_report.png"></code>
<code><img width="5%" title="Allure TestOps" src="design/icons/allure-testops.png"></code>
<code><img width="5%" title="Jira" src="design/icons/jira.png"></code>
<code><img width="5%" title="Telegram" src="design/icons/tg.png"></code>

### Test cases:
- Search:
  - Search results render for valid search query
  - Search for invalid query doesn't return results
- Article:
  - Article successfully opens
- Onboarding:
  - Onboarding screens have correct titles
- Language switch:
  - Language is successfully added to the list of languages

### For local launch:

1. Create a new directory on your local machine

```bash
mkdir mobile_wiki_diploma
cd mobile_wiki_diploma
```

2. Clone the repository

```bash
git clone https://github.com/AngPawl/mobile_wiki_diploma
```

3. Create and fill in `.env` file based on env.example in the root project directory

4. Install and activate virtual environment

```bash
python -m venv .venv
```
  - For Linux/macOs:
  ```bash
  source .venv/bin/activate
  ```
  - For Windows:
  ```bash
  source venv/scripts/activate
  ```

5. Install Poetry package

```bash
pip install poetry
```

6. Install dependencies:

```bash
poetry install
```

7. Launch tests from command line

```bash
pytest .
```

## Remote run is executed on <a target="_blank" href="https://www.browserstack.com/">Browserstack</a> server via <a target="_blank" href="https://jenkins.autotests.cloud/job/007-ang_pawl-mobile_wiki_diploma/">Jenkins</a> job

### For remote launch:
- Open <a target="_blank" href="https://jenkins.autotests.cloud/job/007-ang_pawl-mobile_wiki_diploma/">Jenkins</a> job
- Click on Build with Parameters button
- Choose parameters and click on Build

![This is an image](design/images/jenkins-job1.png)
![This is an image](design/images/jenkins-job2.png)

### You may set the following parameters:
- android_platformVersion (tests will run on this specific platform version): 12.0, 13.0, 11.0
- android_deviceName (device name): Samsung Galaxy S22 Ultra, Google Pixel 7 Pro, OnePlus 9
- timeout: 10s on default

### *After the test run is completed you may check result info and related graphics on Allure Report page:*

![This is an image](design/images/allure-report1.png)

### *You may also look through detailed result info for each test case:*

![This is an image](design/images/allure-report2.png)

## General test run statistics, including manual tests, are stored on <a target="_blank" href="https://allure.autotests.cloud/project/3788/dashboards">Allure TestOps</a> platform

### *Main Allure TestOps dashboard:*

![This is an image](design/images/allure-testops1.png)

### *Full list of automated and manual test cases:*

![This is an image](design/images/allure-testops2.png)

### *Automated and manual tests launch logs:*

![This is an image](design/images/allure-testops3.png)

## Test cases and run results are integrated with <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-958">Atlassian Jira</a> and linked to the corresponding task

![This is an image](design/images/jira.png)

## Additionally, Telegram integration is set for immediate test result notifications:
![This is an image](design/images/tg.png)

### There is a short video sample of a test case run from <a target="_blank" href="https://www.browserstack.com/">Browserstack</a> server
![Watch the video](design/video/test.gif)


REM pytest -s -v -m "sanity" --html=./Reports/report.html testCases --browser chrome
REM pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser chrome
REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases --browser chrome
REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases --browser chrome
pytest -s -v --alluredir= "C:\Users\HP\PycharmProjects\SeleniumWithPythonProjects\OrangeHRM\Reports\reports" C:\Users\HP\PycharmProjects\SeleniumWithPythonProjects\OrangeHRM\testCases
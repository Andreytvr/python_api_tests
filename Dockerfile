FROM python
WORKDIR /python_api_tests/
COPY requirements.txt .
RUN pip install -r requirements.txt 
ENV ENV=.env
CMD python -m pytest -s --alluredir=allure_result && chmod 777 -R ./allure_result
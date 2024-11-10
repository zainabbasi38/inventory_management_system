# base image
FROM python:3.12.5

# setup working directory in container
WORKDIR /inventory_management_system

# copy all files to inventory_management_system directory
COPY . /inventory_management_system/

RUN pip install poetry
 
RUN poetry install

# command to run on container start
CMD ["poetry", "run", "python", "main.py","inventory_management_system/main.py"]
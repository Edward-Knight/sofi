# official base image
FROM python:3.6

# install pipenv
RUN pip install pipenv

# copy over project and run make targets
WORKDIR /usr/src/sofi
COPY . .
RUN make setup install build

# run tests
CMD make test system_test

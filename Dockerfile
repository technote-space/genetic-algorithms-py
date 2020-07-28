FROM python:3.7 as python-base
COPY Pipfile* ./
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT
RUN pip install pipenv
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --ignore-pipfile

FROM python:3.7-slim
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT
COPY --from=python-base $PYROOT/lib/ $PYROOT/lib/
COPY src/ ./src

ENTRYPOINT ["python", "./src/app.py"]
CMD ["cart-pole"]

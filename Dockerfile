FROM jupyter/minimal-notebook

WORKDIR /usr/src/app

ADD requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN easy_install gensim

ADD . .
FROM ubuntu:18.04

RUN sed -i 's/archive.u/ru.archive.u/g' /etc/apt/sources.list \
	  && apt-get update && \
      apt-get install -y --no-install-recommends \
      python3-pip git \
      gcc g++ scons pkg-config \
      libpulse-dev libao-dev libao4 \
      festival festvox-kallpc16k festvox-ru \
      && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U setuptools

RUN git clone --depth=1 https://github.com/Olga-Yakovleva/RHVoice.git /RHVoice \
    && cd /RHVoice && rm -rf .git && scons && scons install && ldconfig

COPY . /ttsdemo
WORKDIR /ttsdemo

RUN python3 -m pip install -Ur optional.txt
RUN python3 -m pip install -Ur requirements.txt

CMD sh -c python3 cleaner.py & python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000

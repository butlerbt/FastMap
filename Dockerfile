FROM continuumio/miniconda:latest

RUN mkdir /usr/src/seg_build_flask_docker
WORKDIR /usr/src/seg_build_flask_docker

COPY environment.yml ./
COPY api.py ./
COPY boot.sh ./

RUN chmod +x boot.sh

RUN conda env create -f environment.yml

RUN echo "source activate flask-env2" > ~/.bashrc
ENV PATH /opt/conda/envs/flask-env2/bin:$PATH

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]


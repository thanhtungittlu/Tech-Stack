#FROM docker-registry.mobio.vn/task_management:latest as cache-image

FROM BE_BASE_COMPILE_IMAGE as compile-image

WORKDIR /home/mobio/projects/task_management
ADD . /home/mobio/projects/task_management

#COPY --from=cache-image /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
#COPY --from=cache-image /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN pip3.8 install -r requirements.txt

# build cython (tùy từng module mở ra)
RUN find src/ -type d -exec sh -c 'if [ ! -f {}/__init__.py ]; then touch {}/__init__.py; fi' \;
RUN python3.8 setup.py build_ext --inplace
RUN find src configs -type f \( -name '*.py' -o -name '*.c' \) -exec rm -f {} \;
RUN rm -rf ./build

FROM BE_BASE_RUN_IMAGE as run-image

ADD . /home/mobio/projects/task_management

ENV LC_ALL=en_US.UTF-8 \
   TASK_MANAGEMENT_HOME=/home/mobio/projects/task_management \
   TASK_MANAGEMENT_FOLDER_NAME=task_management 

ENV data_dir=$APPLICATION_DATA_DIR$TASK_MANAGEMENT_FOLDER_NAME 

   
RUN mkdir -p $data_dir $log_dir $monitor_log_dir

WORKDIR $TASK_MANAGEMENT_HOME

COPY --from=compile-image /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
#COPY --from=compile-image /usr/local/lib64/python3.8/site-packages /usr/local/lib64/python3.8/site-packages
COPY --from=compile-image /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN #yum install -y file-devel

RUN chmod +x *.sh

CMD tail -f /dev/null
FROM tensorflow/serving:2.8.0-rc1

COPY ./output/serving_model /models/model-resiko-kredit
COPY ./config /model_config

ENV MODEL_BASE_PATH=/models
ENV MODEL_NAME=model-resiko-kredit
ENV MONITORING_CONFIG="/model_config/prometheus.config"
#ENV PORT=8501 -- tidak diperlukan. PORT ditentukan oleh heroku

RUN echo '#!/bin/bash \n\n\
tensorflow_model_server --port=8500 --rest_api_port=${PORT} \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh

CMD ["--monitoring_config_file=/model_config/prometheus.config"]

ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]
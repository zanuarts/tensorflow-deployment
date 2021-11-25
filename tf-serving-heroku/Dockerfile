FROM tensorflow/serving:2.2.0

COPY . /models
ENV MODEL_NAME=fashion-mnist

# Workaround for Heroku
# https://devcenter.heroku.com/articles/container-registry-and-runtime#dockerfile-commands-and-runtime

ENV PORT=8501
RUN echo '#!/bin/bash \n\n\
env \n\
tensorflow_model_server --port=8500 --rest_api_port=${PORT} \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh
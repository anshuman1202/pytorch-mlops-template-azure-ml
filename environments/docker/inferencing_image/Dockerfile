FROM 4d3602983f8547aa8deaeb9718806017.azurecr.io/azureml/azureml_6a37a53f7e2a047b2229daa462a37c7b
ENV AZUREML_MODEL_DIR=/var/azureml-app/azureml-models/dog_clf_model/1
COPY azureml-app /var/azureml-app
RUN mkdir -p '/var/azureml-app' && echo eyJhY2NvdW50Q29udGV4dCI6eyJzdWJzY3JpcHRpb25JZCI6ImU1OGEyM2RhLTQyMWUtNGI1Mi05OWQ1LWU2MTVmMmY4YmU0MSIsInJlc291cmNlR3JvdXBOYW1lIjoibWxvcHN0ZW1wbGF0ZXJnIiwiYWNjb3VudE5hbWUiOiJtbG9wc3RlbXBsYXRld3NiZmRjMjQiLCJ3b3Jrc3BhY2VJZCI6IjRkMzYwMjk4LTNmODUtNDdhYS04ZGVhLWViOTcxODgwNjAxNyJ9LCJtb2RlbHMiOnsiZG9nX2NsZl9tb2RlbCI6eyJ2ZXJzaW9uIjoxLCJpZCI6ImRvZ19jbGZfbW9kZWw6MSIsImludGVybmFsSWQiOiI2NTJjMzhmNDNhN2Q0M2Y4YmViOWQxOWNmMjVlZGY0ZCJ9fSwibW9kZWxzSW5mbyI6eyJkb2dfY2xmX21vZGVsIjp7IjEiOnsidmVyc2lvbiI6MSwiaWQiOiJkb2dfY2xmX21vZGVsOjEiLCJpbnRlcm5hbElkIjoiNjUyYzM4ZjQzYTdkNDNmOGJlYjlkMTljZjI1ZWRmNGQiLCJkYXRhQ29sbGVjdG9yU3RvcmFnZVBhdGgiOiIvbW9kZWxkYXRhL2U1OGEyM2RhLTQyMWUtNGI1Mi05OWQ1LWU2MTVmMmY4YmU0MS9tbG9wc3RlbXBsYXRlcmcvbWxvcHN0ZW1wbGF0ZXdzYmZkYzI0L3t3ZWJzZXJ2aWNlX25hbWV9L2RvZ19jbGZfbW9kZWwvMS8ifX19fQ== | base64 --decode > /var/azureml-app/model_config_map.json
RUN mv '/var/azureml-app/tmp3ktheggt.py' /var/azureml-app/main.py
CMD ["runsvdir","/var/runit"]
